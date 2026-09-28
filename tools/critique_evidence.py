"""Portable source-quotation checks. Python 3.10+, standard library only.

Checks attribution, not interpretation or creative quality. Receipts detect
changed inputs; they are not signatures against deliberate forgery.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

TEXT_FIELDS = ("diagnosis", "gap", "structural_note", "proposed_rewrite")
REPORT_FIELDS = set(TEXT_FIELDS) | {"in_place_directives", "evidence"}
VERSION = 1


class EvidenceError(ValueError):
    """A report or its supporting inputs cannot be verified."""


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=True, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def validate_sources(sources):
    if not isinstance(sources, dict) or not isinstance(sources.get("draft"), str):
        raise EvidenceError("INVALID_SOURCES")
    allowed = {"draft", "exemplar:1", "exemplar:2", "exemplar:3"}
    if not set(sources) <= allowed or not all(isinstance(v, str) for v in sources.values()):
        raise EvidenceError("INVALID_SOURCES")


def validate_critique(payload, sources):
    """Raise EvidenceError on failure; return no trusted model metadata."""
    validate_sources(sources)
    if not isinstance(payload, dict) or set(payload) != REPORT_FIELDS:
        raise EvidenceError("INVALID_REPORT_FIELDS")
    if not all(isinstance(payload[key], str) for key in TEXT_FIELDS):
        raise EvidenceError("INVALID_REPORT_TEXT")
    directives = payload["in_place_directives"]
    if not isinstance(directives, list) or not all(
        isinstance(item, str) and item.strip() for item in directives
    ):
        raise EvidenceError("INVALID_DIRECTIVES")
    evidence = payload["evidence"]
    if not isinstance(evidence, list) or not 1 <= len(evidence) <= 8:
        raise EvidenceError("EVIDENCE_REQUIRED")
    has_draft = False
    for item in evidence:
        if not isinstance(item, dict) or set(item) != {"source", "quote"}:
            raise EvidenceError("INVALID_EVIDENCE_FIELDS")
        source, quote = item["source"], item["quote"]
        if not isinstance(source, str) or source not in sources:
            raise EvidenceError("UNKNOWN_EVIDENCE_SOURCE")
        if not isinstance(quote, str) or not quote.strip() or len(quote) > 1000:
            raise EvidenceError("INVALID_EVIDENCE_QUOTE")
        if quote not in sources[source]:
            raise EvidenceError("QUOTE_NOT_IN_NAMED_SOURCE")
        has_draft = has_draft or source == "draft"
    if not has_draft:
        raise EvidenceError("DRAFT_EVIDENCE_REQUIRED")


def receipt(payload, sources, script_bytes):
    validate_critique(payload, sources)
    return {"version": VERSION, "report_sha256": digest(payload),
            "sources_sha256": digest(sources),
            "script_sha256": hashlib.sha256(script_bytes).hexdigest()}


def verify(saved, sources, script_bytes):
    if not isinstance(saved, dict) or set(saved) != {"report", "verification"}:
        raise EvidenceError("INVALID_VERIFIED_REPORT")
    expected = receipt(saved["report"], sources, script_bytes)
    if saved["verification"] != expected:
        raise EvidenceError("STALE_OR_EDITED_REPORT")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise EvidenceError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def read_json(path):
    # Preserve escaped source whitespace exactly. JSON duplicates are rejected.
    return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                      object_pairs_hook=_unique_object)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "check"):
        command = commands.add_parser(name)
        command.add_argument("--sources", required=True)
        command.add_argument("--report", required=True)
        command.add_argument("--script", required=True,
                             help="Full current screenplay file, hashed without modification")
        if name == "validate":
            command.add_argument("--output", required=True,
                                 help="New receipt file; never overwrites an existing file")
    args = parser.parse_args(argv)
    try:
        sources = read_json(args.sources)
        report = read_json(args.report)
        script_bytes = Path(args.script).read_bytes()
        if args.command == "validate":
            saved = {"report": report, "verification": receipt(report, sources, script_bytes)}
            encoded = json.dumps(saved, ensure_ascii=True, indent=2) + "\n"
            with Path(args.output).open("x", encoding="utf-8", newline="\n") as output:
                output.write(encoded)
        else:
            verify(report, sources, script_bytes)
    except EvidenceError as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1
    except (OSError, UnicodeError, ValueError, TypeError):
        # Do not leak screenplay text or private paths through exception output.
        print("BLOCKED: INPUT_OR_OUTPUT_ERROR", file=sys.stderr)
        return 1
    print("PASS: source quotations match; interpretations and rewrites remain unverified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
