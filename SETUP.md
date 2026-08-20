# Setup

## Claude Code (local machine)

Clone anywhere, then point a skill at it, or simply clone to the path the bundled
skill expects:

```bash
git clone https://github.com/hernanyperla-design/screenplay-craft ~/screenplay-craft
mkdir -p ~/.claude/skills/screenplay-craft
cp ~/screenplay-craft/skill/SKILL.md ~/.claude/skills/screenplay-craft/SKILL.md
```

New sessions pick it up automatically. To update, `git pull` in `~/screenplay-craft`.
The skill reads the codex from the clone, so pulling is the whole update.

## Cowork or any cloud session

The bundled skill clones this repository itself on first use, so there is nothing
to install ahead of time. Add the skill once to your profile and every session
pulls the current codex on its own.

## Updating the doctrine

Edit `codex/craft-codex.md`, commit, push. Every environment picks it up on its
next session. There is no build step and no second copy to keep in sync.
