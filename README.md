# screenplay-craft

Portable screenplay craft doctrine, packaged as a Claude skill.

The shared craft master is [`codex/craft-codex.md`](codex/craft-codex.md),
an accumulated set of craft rules for writing and revising screenplays. Story
architecture, structure, dialogue subtext, action-line economy, opening hooks,
mystery information management, physical suspense, backstory function, and
revision discipline.

The doctrine remains portable text. A standard-library Python validator now checks
source quotations and rejects stale critique receipts. It needs Python 3.10+ but
no API keys, packages, or private corpus. See [EVIDENCE.md](EVIDENCE.md).

## What this is not

This is the shared knowledge and evidence-validation layer of a larger system.
Generation, corpus retrieval, screenplay rewriting, and PDF-annotation sync remain
separate local tools. Cloud sessions use [WORKFLOW.md](WORKFLOW.md) and the portable
validator; publishing the checker does not make unrelated apps execute it.

The elite-screenplay corpus that the critique tool scores against is copyrighted
source material and is deliberately absent from this repository.

## Install

See [SETUP.md](SETUP.md).

Run the portable regression suite with `python3 -m unittest discover -s tests -v`.
Tests contain synthetic text only and make no API calls.

## Status

Sections I through V are stable doctrine. Sections marked **working draft** are in
active validation against real scripts and may change, move, or be removed. They
are labelled rather than hidden, because knowing which rules are load-bearing and
which are provisional is part of using them well.

The September 2026 working-draft additions cover commercial-thriller readability,
exposition under pressure, physical suspense, present-tense backstory function, and
revision provenance. They contain generalized doctrine only. No private screenplay
text or project canon is stored here.

See [EVALUATION.md](EVALUATION.md) for the blind preference, held-out project,
and mechanical gates required before any rule becomes stable or any claim of
professional parity is made.

## Licence

Not yet chosen. Until one is added, treat this as all rights reserved.
