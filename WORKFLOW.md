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

**Genre sections.** Name the genre sections that apply at the same time: Section VII
when hidden information is the engine, Section IX for a commercial thriller. Where two
sections pull against each other, the one named for the project governs. The writer's
hand notes outrank both.

### The Strip-the-Diction Test

In dialog-forward register, read the dialogue alone. Can you follow the essential
situation, who wants what, and what is at stake? When one missing fact belongs
to a visual discovery or a deliberate silence, restore the action and check the
next choice before adding a line. Honor a brief that calls for the entire plot
to play in dialogue alone.

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
6. **Does the exchange give the reader the orientation this register calls for?**
7. **Are the action lines filmable, geographically clear, and physically suspenseful?**

## Working method

Preserve the project's established source format. Use Fountain as a useful default only
when a new project has no source-of-truth format. An established FDX project stays FDX;
temporary conversions never silently replace it. Critique per act against the codex,
revise only within the approved scope, and compile the final deliverable last.

When the writer asks to discuss notes first, diagnose and recommend without editing.
For cuts, an abrupt reversal or competing pressures, use the relevant question in
[Revision decisions](REVISION-DECISIONS.md). Its genre questions are candidates.
Promote a new craft rule only after writer approval, blind comparison, complete mechanical
validation, and a held-out check against other projects or registers.

For system-level changes or claims of professional parity, follow `EVALUATION.md` in the
repository. Never use the model's self-score as proof that the writing is professional.

## Act-level rewrite protocol (candidate)

Candidate. Drawn from one project and one reader, and not yet blind tested. Use it when an
act or a long sequence has to be rebuilt. It is not for line edits or a single scene.

1. Read the whole current draft straight through, and every note the writer left on it,
   before proposing anything. Read each note against the page it sits on.
2. Reply in one message with no pages in it: what the notes have in common, a one-page
   chain of beats linked by "therefore" or "but" (never "and then"), what the reference
   scripts do at the same point in their stories, and the two or three decisions only the
   writer can make.
3. List what is already planted on the page. A new scene pays off a plant before it
   invents new machinery.
4. Name the one sentence the act turns on, a claim both leads have a stake in.
5. Read reference scripts with a question, for mechanism and not for style.
6. Write nothing until the writer has approved the chain and answered the decisions.
7. Write one act per pass, in one sitting. Stop for the writer's read before the next act.
8. Run mechanical checks last: format, speaker cues, a diff against the previous pass.
   They are not evidence that the pages work.

Why it is a candidate: on one script the same model at the same settings wrote a final
act the writer threw out and, days later, a replacement he approved on first read. The
first was written before he had read that stretch, from a list of principles, in several
passes with no read between them. The second followed the steps above. Genre does not
change the steps. It changes which reference scripts are read and which register rules
apply.

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
