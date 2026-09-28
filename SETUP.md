# Setup

## Local or cloud code sessions

Clone the master and install the skill once:

```bash
git clone https://github.com/hernanyperla-design/screenplay-craft ~/screenplay-craft
mkdir -p ~/.claude/skills/screenplay-craft
cp ~/screenplay-craft/skill/SKILL.md ~/.claude/skills/screenplay-craft/SKILL.md
```

The bootstrap refreshes the checkout and reads the current codex and workflow on
each invocation. It reports update failures instead of silently claiming freshness.
For a cloud product with a skill-upload interface, install `skill/SKILL.md` there;
the filesystem installation above is for environments exposing those directories.

Python 3.10+ is needed for mechanical evidence checking. No pip install is needed.
Follow `EVIDENCE.md` for the two commands: validate quotations, then recheck the
receipt immediately before applying approved revisions. A cloud environment must
allow code execution for this enforcement. Without execution, notes remain
unverified and cannot drive automatic revisions.

## Existing installations

An older installed skill already pulls the repository and reads the codex. The
codex now directs it to `EVIDENCE.md` and the validator, so a successful refresh
delivers this improvement without reinstalling the skill. Replacing the installed
skill with the new bootstrap also makes workflow updates and refresh-failure
reporting explicit. Restart or reinvoke the skill in an already-running session;
an existing conversation does not refresh itself merely because GitHub changed.

To inspect the version and check for updates manually:

```bash
git -C ~/screenplay-craft status --short
git -C ~/screenplay-craft pull --ff-only origin main
git -C ~/screenplay-craft rev-parse HEAD
```

Preserve local changes. Do not force-reset a checkout to update it.

## One master

Edit shared doctrine, `WORKFLOW.md`, `EVIDENCE.md`, or the validator in this
repository. Run tests, commit, and push. Environments receive the changes on their
next successful refresh. Local Python integrations should import
`tools/critique_evidence.py` from this checkout instead of copying its logic.

The inbound-polish integration resolves the checkout at `~/screenplay-craft` by
default, with `SCREENPLAY_CRAFT_ROOT` as an optional override. Its private rewrite
engine and corpus are not published here.

Keep source snapshots, critiques, receipts, scripts, and private examples in a
project working directory outside this public repository.
