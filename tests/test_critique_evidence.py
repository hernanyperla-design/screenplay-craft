"""Synthetic, offline tests for the portable public validator."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import critique_evidence as ev

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {"draft": "MARA\nKeep the key.",
           "exemplar:1": "He leaves the key on the table."}
REPORT = {"diagnosis": "Interpretation: evidence 1 suggests responsibility.",
          "gap": "Suggestion: clarify the handoff.",
          "in_place_directives": ["Clarify the action."],
          "structural_note": "", "proposed_rewrite": "Mara leaves the key.",
          "evidence": [{"source": "draft", "quote": "Keep the key."}]}


class EvidenceTests(unittest.TestCase):
    def test_exact_quotes_from_both_sources(self):
        report = copy.deepcopy(REPORT)
        report["evidence"].append({"source": "exemplar:1", "quote": "He leaves the key"})
        ev.validate_critique(report, SOURCES)

    def test_bad_evidence(self):
        for evidence in ([], None, "quote", [None],
                         [{"source": "draft", "quote": "Invented."}],
                         [{"source": "draft", "quote": "Keep  the key."}],
                         [{"source": "draft", "quote": "He leaves the key"}],
                         [{"source": "exemplar:1", "quote": "Keep the key."}],
                         [{"source": "exemplar:2", "quote": "Keep the key."}],
                         [{"source": "exemplar:1", "quote": "He leaves the key"}],
                         [{"source": [], "quote": "Keep the key."}],
                         [{"source": "draft", "quote": " "}],
                         [{"source": "draft", "quote": "x" * 1001}],
                         [{"source": "draft", "quote": 1}],
                         [{"source": "draft", "quote": "Keep the key.", "verified": True}],
                         REPORT["evidence"] * 9):
            with self.subTest(evidence=evidence):
                report = {**REPORT, "evidence": evidence}
                with self.assertRaises(ev.EvidenceError):
                    ev.validate_critique(report, SOURCES)

    def test_invalid_reports_and_model_metadata(self):
        for report in (None, [], {}, {**REPORT, "gap": None},
                       {**REPORT, "in_place_directives": [False]},
                       {**REPORT, "in_place_directives": "rewrite"},
                       {**REPORT, "evidence_validated": True}):
            with self.subTest(report=report), self.assertRaises(ev.EvidenceError):
                ev.validate_critique(report, SOURCES)

    def test_unicode_and_whitespace(self):
        source = "Caf\u00e9.\n  Keep the key."
        report = {**REPORT, "evidence": [{"source": "draft", "quote": source}]}
        ev.validate_critique(report, {"draft": source})
        with self.assertRaises(ev.EvidenceError):
            ev.validate_critique(report, {"draft": source.replace("\n  ", " ")})

    def test_invalid_sources(self):
        for sources in (None, [], {}, {"draft": None}, {**SOURCES, "exemplar:4": "text"}):
            with self.subTest(sources=sources), self.assertRaises(ev.EvidenceError):
                ev.validate_critique(REPORT, sources)

    def test_receipt_round_trip(self):
        saved = {"report": REPORT, "verification": ev.receipt(REPORT, SOURCES, b"full script")}
        ev.verify(json.loads(json.dumps(saved)), SOURCES, b"full script")

    def test_edits_invalidate_receipt(self):
        for mutation in ("report", "sources", "script", "version"):
            with self.subTest(mutation=mutation):
                sources = copy.deepcopy(SOURCES)
                script = b"full script"
                saved = {"report": copy.deepcopy(REPORT),
                         "verification": ev.receipt(REPORT, sources, script)}
                if mutation == "report":
                    saved["report"]["gap"] = "Another suggestion."
                elif mutation == "sources":
                    sources["exemplar:1"] += " An uncited change."
                elif mutation == "script":
                    script += b" Change beyond supplied excerpt."
                else:
                    saved["verification"]["version"] = 999
                with self.assertRaises(ev.EvidenceError):
                    ev.verify(saved, sources, script)

    def test_legacy_report_cannot_pass_check(self):
        with self.assertRaises(ev.EvidenceError):
            ev.verify(REPORT, SOURCES, b"script")


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sources = self.root / "sources.json"
        self.report = self.root / "report.json"
        self.script = self.root / "current.fdx"
        self.output = self.root / "verified.json"
        self.sources.write_text(json.dumps(SOURCES), encoding="utf-8")
        self.report.write_text(json.dumps(REPORT), encoding="utf-8")
        self.original = b'<FinalDraft><Text RevisionID="1">Keep the key.</Text></FinalDraft>'
        self.script.write_bytes(self.original)

    def run_command(self, command):
        args = [sys.executable, str(ROOT / "tools" / "critique_evidence.py"), command,
                "--sources", str(self.sources), "--script", str(self.script),
                "--report", str(self.report if command == "validate" else self.output)]
        if command == "validate":
            args += ["--output", str(self.output)]
        return subprocess.run(args, capture_output=True, text=True)

    def test_validate_and_check_preserve_script(self):
        self.assertEqual(self.run_command("validate").returncode, 0)
        self.assertEqual(self.run_command("check").returncode, 0)
        self.assertEqual(self.script.read_bytes(), self.original)

    def test_invalid_quote_writes_no_receipt(self):
        report = copy.deepcopy(REPORT)
        report["evidence"][0]["quote"] = "Invented."
        self.report.write_text(json.dumps(report), encoding="utf-8")
        self.assertEqual(self.run_command("validate").returncode, 1)
        self.assertFalse(self.output.exists())
        self.assertEqual(self.script.read_bytes(), self.original)

    def test_output_never_overwrites_existing_file(self):
        self.output.write_text("preserve me", encoding="utf-8")
        self.assertEqual(self.run_command("validate").returncode, 1)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "preserve me")

    def test_stale_script_fails_check(self):
        self.assertEqual(self.run_command("validate").returncode, 0)
        self.script.write_bytes(self.original + b" changed")
        self.assertEqual(self.run_command("check").returncode, 1)

    def test_malformed_or_duplicate_json_fails_closed(self):
        for content in ('{invalid}', '{"draft":"one","draft":"two"}'):
            with self.subTest(content=content):
                self.sources.write_text(content, encoding="utf-8")
                result = self.run_command("validate")
                self.assertEqual(result.returncode, 1)
                self.assertFalse(self.output.exists())
                self.assertNotIn("Keep the key", result.stderr)

    def test_missing_input_is_reported_without_script_text(self):
        self.sources.unlink()
        result = self.run_command("validate")
        self.assertEqual(result.returncode, 1)
        self.assertIn("INPUT_OR_OUTPUT_ERROR", result.stderr)


if __name__ == "__main__":
    unittest.main()
