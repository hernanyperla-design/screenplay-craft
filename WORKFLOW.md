---
name: screenplay-workflow
description: Current shared workflow, loaded by the installed screenplay-craft bootstrap.
---

# Screenplay Craft

Read this workflow from the GitHub master, not from a remembered installed copy.

## Step 1 - get the current codex

The installed bootstrap handles refresh. If this file was reached through an older
skill, check for local changes and refresh the clean checkout with:

```bash
git -C ~/screenplay-craft status --porcelain
git -C ~/screenplay-craft pull --ff-only origin main
```

Do not pull over local modifications. Do not discard or stash changes. If refresh
fails, disclose the failure and the cached commit rather than claiming freshness.

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
| IX | Commercial thriller readability, exposition under pressure, physical suspense | Working draft |
| X | Backstory, trauma, and present-tense dramatic function | Working draft |
| XI | Revision provenance, native-format preservation, validation | Working draft |

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
6. **Can a dialogue-skimming reader follow the discovery, objective, and danger?**
7. **Are the action lines filmable, geographically clear, and physically suspenseful?**

## Working method

Preserve the project's established source format. Use Fountain as a useful default only
when a new project has no source-of-truth format. An established FDX project stays FDX;
temporary conversions never silently replace it. Critique per act against the codex,
revise only within the approved scope, and compile the final deliverable last.

When the writer asks to discuss notes first, diagnose and recommend without editing.
Promote a new craft rule only after writer approval, blind comparison, complete mechanical
validation, and a held-out check against other projects or registers.

For system-level changes or claims of professional parity, follow `EVALUATION.md` in the
repository. Never use the model's self-score as proof that the writing is professional.

## Source-based critique and revision

Follow `EVIDENCE.md` and run the shared validator before presenting a source-based
critique as mechanically verified. Recheck against the current screenplay before
applying the approved batch of edits. Do not let failed, stale, or legacy reports
drive automatic revisions. Passing attribution checks does not validate taste,
interpretation, completeness of evidence, or creative quality.

## Scope

Craft doctrine can be applied by a person or a model. Source-quotation validation
also includes a small portable Python tool, available in local and cloud checkouts.
The private corpus and screenplay rewrite engine remain separate local tools.
