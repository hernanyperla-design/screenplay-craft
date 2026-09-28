---
name: screenplay-craft
description: Shared screenplay writing, revision, and critique doctrine. Use for screenplay, pilot, treatment, scene, dialogue, and script-note work. Loads current doctrine and source-evidence validation from the screenplay-craft GitHub master. Mechanical quote checks require Python 3.10+.
---

# Screenplay Craft

This is a bootstrap. Keep workflow instructions in the repository, so an installed
copy of this skill can load future improvements without being reinstalled.

## Refresh the master on each invocation

Use the user's existing `~/screenplay-craft` checkout. Clone it if missing:

```bash
git clone --depth 1 https://github.com/hernanyperla-design/screenplay-craft ~/screenplay-craft
```

For an existing checkout, check for local modifications first:

```bash
git -C ~/screenplay-craft status --porcelain
```

If clean, update the checkout with:

```bash
git -C ~/screenplay-craft pull --ff-only origin main
```

Do not reset, stash, switch branches, or overwrite local changes automatically.
If refresh fails, or local changes prevent it, report that the master was not
refreshed and identify the available commit. Do not claim an offline or modified
copy is current. An available cached version may still be used with that caveat.
If no checkout is available, state the limitation rather than inventing its rules.

## Read the shared instructions

Read these from the refreshed checkout before doing craft work:

1. `codex/craft-codex.md`
2. `WORKFLOW.md`
3. `EVIDENCE.md` when critiquing existing source material or applying those notes

Follow the source-quote validator and revision check in `EVIDENCE.md`. If execution
is unavailable, label notes unverified and do not automatically apply them.

The repository contains no private screenplay corpus. Use only source material
actually supplied in the session. Existing user authorization governs the scope
of revisions; passing validation does not grant additional authority.
