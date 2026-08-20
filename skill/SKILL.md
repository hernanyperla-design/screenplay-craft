---
name: screenplay-craft
description: Portable screenplay craft doctrine covering story architecture, structure, dialogue subtext, visual action lines, opening hooks, mystery information management, and payoff auditing. Use whenever writing, revising, critiquing, or evaluating a screenplay, pilot, treatment, scene, or dialogue pass, and whenever judging whether a draft is working and why. Also use when giving script notes or diagnosing why an opening, an ending, or a character arc falls flat. Pure knowledge with no local dependencies, so it works identically in Claude Code, cloud sessions, and on any machine. Pulls the current codex from a public git repository on invoke, so the doctrine is never stale.
---

# Screenplay Craft

The portable doctrine layer. Everything is text, so this works the same everywhere.

## Step 1 - get the current codex

Run this first, every time. It clones on first use and updates on every use after,
so the doctrine you read is always current:

```bash
if [ -d ~/screenplay-craft/.git ]; then
  git -C ~/screenplay-craft pull --quiet 2>/dev/null || true
else
  git clone --depth 1 --quiet https://github.com/hernanyperla-design/screenplay-craft ~/screenplay-craft
fi
```

The pull is allowed to fail silently. If there are uncommitted local edits, or the
network is down, the existing clone is still read rather than lost.

Then read `~/screenplay-craft/codex/craft-codex.md`.

If the network is unavailable and no clone exists, say so plainly and work from the
principles below. Do not invent doctrine to fill the gap.

## Step 2 - read the codex before doing craft work

Read the file. Do not work from memory of these principles, because the codex changes
as techniques get validated, and a half-remembered version will be subtly wrong in
exactly the places that matter.

| Section | Covers | Status |
|---|---|---|
| I | Story architecture, controlling idea, Want/Need/Flaw, conflict engine | Stable |
| II | Structure, Save the Cat hybrid, G.O.D.D. scene test, arrive late/leave early | Stable |
| III | Dialogue, subtext first, naturalistic rhythm, strategic pauses | Stable |
| IV | Visual and action lines, economy, active verbs, no unfilmable interiority | Stable |
| V | Format rules | Stable |
| VI | Opening hook construction, five levers with a scored diagnostic | Working draft |
| VII | Mystery and information craft, twelve principles | Working draft |
| VIII | The payoff audit, Chekhov's gun in both directions | Working draft |

Apply stable sections freely. Apply working drafts too, but tell the writer they are
provisional and note what worked, since results feed the decision to promote them.

## Register: ask once, then hold

Establish this before drafting anything substantial. It governs everything downstream
and should not drift mid-script.

**Visual-first.** Action verbs only, no interiority on the page, roughly 40 to 60 pages
of tight behavioural writing. Right for action thrillers and festival shorts.

**Dialog-forward.** Articulated distinct voices, controlled interiority permitted in
action lines, long scenes that carry real weight, roughly 90 to 110 pages. Right for
prestige features and character thrillers.

### The Strip-the-Diction Test

In dialog-forward register, strip every action line and read only the dialogue. The
story must still come through. If it does not, the dialogue is leaning on stage
direction to carry meaning it should carry itself.

## Diagnostic order when a draft is not working

Work top-down. A structural problem cannot be fixed at the line level, so polishing
dialogue on a broken spine wastes the pass.

1. **Is the controlling idea coherent?** If theme, character architecture, and conflict
   contradict each other, nothing below matters.
2. **Is there an active antagonist?** A protagonist facing only external obstacles with
   no opposing force produces diffuse tension. Common, and usually invisible to the writer.
3. **Does the protagonist cause the ending?** If the climax resolves through arrival,
   windfall, or coincidence, that is a payoff failure. Restructure rather than polish.
4. **Does every scene pass G.O.D.D.?**
5. **Is the dialogue carrying subtext?**
6. **Are the action lines filmable?**

## Working method

Draft and revise in Fountain, treating it as the working source. Critique per act
against the codex, expecting two or three cycles per act in dialog-forward and one or
two in visual-first. Revise on the notes, changing only what each note calls for.
Compile the final deliverable last.

## Scope

This skill is doctrine, not automation. Separate local tools exist that automate some
of these passes against a private corpus, but they are not required and are not
available in cloud sessions. Everything here is executable by hand.
