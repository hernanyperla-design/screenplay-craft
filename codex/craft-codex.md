# HARTBEAT Craft Codex

Accumulated screenplay craft doctrine.

**This file is the source of truth for the craft layer.** Edit it here. The local
toolchain reads it directly, and `build-craft-skill.py` syncs it into the portable
`screenplay-craft` skill so Cowork and any other machine get the same doctrine.

Sections I-V are stable. Sections marked **working draft** are in active validation
against real scripts and may change, move, or be removed.

---

## I. Story Architecture

### Controlling Idea
Every great script is an argument. State the central thematic argument in one sentence:
> "When [situation], [outcome] because [reason]."

### Character Architecture
For each major character:
- **Conscious Want** — the external goal the character believes they need
- **Unconscious Need** — what the character actually needs to grow or survive
- **Fatal Flaw** — the specific trait or belief that blocks them from what they need
- **Arc Summary** — one sentence: transformation from flaw to growth (or tragic failure)

### Core Conflict Engine
- **External Conflict** — the tangible, visible struggle
- **Internal Conflict** — the psychological battle within the protagonist
- **Thematic Conflict** — the philosophical tension the story explores

---

## II. Structural Blueprint (Save the Cat / 8-Sequence Hybrid)

| Beat | Pages | Function |
|------|-------|----------|
| Opening Image | 1–3 | Visual thesis — the protagonist's world BEFORE the story changes them |
| Theme Stated | 5–7 | Someone (not the protagonist) states the lesson. Goes unrecognized. |
| Set-Up | 1–12 | Status quo, relationships, flaws, world |
| Catalyst | 12–15 | Disrupts the status quo. Life as they know it is over. |
| Debate | 15–25 | Protagonist resists the call. Last moment of hesitation. |
| Break into Two | 25–30 | Protagonist makes a CHOICE (not forced) to enter Act Two |
| B-Story | 30–35 | Subplot (love interest, mentor) carrying the thematic argument |
| Fun and Games | 30–55 | The promise of the premise. Trailer moments. |
| Midpoint | 55 | False victory or false defeat. Stakes raised — no longer a game. |
| Bad Guys Close In | 55–75 | Pressures mount. Flaws resurface. Team fractures. |
| All Is Lost | 75 | Lowest point. A "whiff of death" — literal or metaphorical. |
| Dark Night of Soul | 75–85 | Despair → glimmer. Theme from Beat 2 finally clicks. |
| Break into Three | 85 | Armed with thematic truth, hero devises a NEW plan. |
| Finale | 85–110 | Confronts antagonist as new self. A-story and B-story merge. Theme proven. |
| Final Image | 110 | Mirror of Opening Image — shows transformation. |

### Scene-Level Rules
- Every scene must have CONFLICT. No scenes where characters simply exchange information pleasantly.
- **G.O.D.D. Test** — each scene must pass:
  - **Goal** — what does the POV character want in this scene?
  - **Obstacle** — what stands in their way right now?
  - **Danger** — what are the stakes if they fail? (emotional, physical, or social)
  - **Direction** — how does the outcome propel us into the next scene?
- **Arrive late** — drop into the middle of the conflict; never open with entering rooms, greetings, or settling in
- **Leave early** — cut the moment the dramatic question is answered; no wrap-up dialogue
- Most scenes run 1–3 pages. Only climactic scenes go longer.
- Vary locations — don't stack consecutive scenes in the same place.
- Alternate high-intensity and breathing-room scenes for pacing.

---

## III. Dialogue Principles

### Subtext — The #1 Priority
- **Flag on-the-nose dialogue.** Any line where a character states exactly what they feel or think must be rewritten.
- **Characters never say what they mean directly.** They:
  - Deflect with humor or sarcasm
  - Talk about something mundane while the real conversation happens underneath
  - Ask questions instead of making statements
  - Use silence or changing the subject as a weapon
  - Lie — and the audience knows they're lying
- Example: Instead of "I'm devastated you're leaving," write a character obsessively organizing a junk drawer while asking "Did you pack the phone charger?"

### Naturalistic Rhythm
- Break up any speech longer than 3–4 lines. People don't monologue in real life.
- Characters INTERRUPT each other — use `--` at the end of cut-off lines
- Sentences trail off with `...` when characters lose nerve or change course
- People repeat themselves. They say "I mean" and "like" and "look" and "right?"
- Each character must have a DISTINCT voice pattern — vocabulary, sentence length, verbal tics

### Strategic Pauses
- Use `(beat)` or `(a moment)` sparingly — maximum 2–3 per scene
- Reserve pauses for moments where subtext SHIFTS — when the unspoken meaning changes
- Never use parentheticals to describe emotions the actor should figure out ("angrily," "sadly")
- Only use parentheticals when the line reading is COUNTERINTUITIVE — when the character says something that could be read multiple ways

### Hard Negative Constraints (Polish Pass)
- Characters may not state their emotional state or the scene's theme directly
- No line may tell another character something they both already know
- Do not rewrite action lines
- Do not add or delete scenes
- Do not rename characters
- Output dialogue only

---

## IV. Visual & Action Line Principles

### Action Line Economy
- **Maximum 4 lines per action block.** If longer, break with white space.
- **Active verbs, present tense.** Kill all "-ing" constructions:
  - BAD: "John is running down the hallway" → GOOD: "John sprints down the hallway"
  - BAD: "She is looking out the window, thinking about her mother" → GOOD: "She presses her forehead to the glass. Breath fogs the pane."
- **No "we see" or "we hear."** Just describe it.
- **Cut adjective/adverb bloat.** One precise word beats three vague ones.

### Visual Storytelling — Show, Don't Tell
- **Eliminate ALL internal states.** Nothing unfilmable:
  - BAD: "She thinks about her dead husband" → GOOD: "She traces the rim of a rusted locket"
  - BAD: "He feels guilty about what he's done" → GOOD: "He scrubs his hands under scalding water. The skin turns pink, then red."
- **Behavior reveals character.** Use physical action, objects, environment to convey emotion.
- **Be specific and concrete.** Not "a photo" — "a Polaroid with a crease down the middle."

### Thematic Atmosphere
- Match the visual language to the story's tone and genre
- Use setting details, weather, light, and objects as thematic motifs
- Let the environment mirror or contrast the character's inner state
- Sound design in prose: ambient sounds that build mood

---

## V. Format Rules

- Scene headings: `INT./EXT. LOCATION - DAY/NIGHT` (all caps)
- Action lines: present tense, active voice, 1–4 line blocks max
- Character names: ALL CAPS on first introduction (with brief, vivid description), then as-written above dialogue
- Dialogue: centered under character name, natural and conversational
- Parentheticals: use SPARINGLY — only when the line reading contradicts the obvious interpretation
- NO camera directions (`we see`, `the camera pans`, `close on`)
- NO character internal thoughts — only filmable behavior
- Courier Final Draft 12pt, standard margins

---

## VI. Opening Hook Construction

> **Working draft (added 2026-05-06).** This section is in test against new scripts and will migrate to `screenplay_pipeline/phases/phase3_scene_construction.py` once the technique-set stabilizes. Sections I–V remain pipeline-snapshotted and read-only.

The opening must hook the audience in the first 30 seconds of screen time (≈1 page). Evaluate every opening against five techniques. A 4/5 opening is strong; 3/5 is fine; 2/5 or below — rebuild.

### Five Techniques

**1. Lead with the Punch.** The strongest beat in the opening — the most arresting image, sound, or line — should land in the first 30 seconds. Not buried at the end of an atmospheric build.
- *Diagnostic:* What page does the strongest beat land on? If not page 1, why?
- *Fix:* Extract the strongest beat. Present it OVER BLACK with a held pause. Then reveal it in scene context. The repetition is not redundant — the audience now *recognizes* the moment as it rebuilds, deepening dread or anticipation.

**2. Audience Implication.** The audience must participate, not observe. Give them information the protagonist does not have. The gap is the hook.
- *Film equivalent of "show of hands":* the line `She doesn't see it. We do.` Dramatic irony in real time.
- *Diagnostic:* What does the audience know that the character does not? When does the gap open?
- *Fix:* At the moment of fear / wonder / threat, cut to the audience-only POV. Show what the character will not see, or hear what they cannot. Use sparingly — once or twice per scene.

**3. Imaginary World — Action Verbs Over Summary.** Concrete physical specificity beats abstract description. The camera sees gestures, not feelings. (Overlaps with §IV but applies to openings with extra force — the first scene cannot afford a single abstract beat.)
- *Diagnostic:* Count verbs in each action paragraph. If a beat is summarized in adjectives ("nervous, panicked, frantic"), it fails. If two physical actions collapse into one verb ("he breaks the door"), break them apart.
- *Fix — collapsed actions:* "He breaks the door." → "He yanks the handle. Locked. He yanks again. Steps back. Kicks the seam."
- *Fix — abstract states:* "She is scared." → "Her fingers find the keyhole. It is empty. She stares at the empty hole."

**4. Big Promise.** Within the first beat, the audience must be able to answer "what kind of story is this?" — even before they know the plot. The "what's in it for me?" If they cannot answer in 60 seconds, they leave. The promise can be plot, tone, theme, or motif. A single sharpened phrase or visual that implies "this is happening on purpose" / "this will recur" / "this is the world we are in" can carry it.
- *Diagnostic:* If a stranger watched only the first 60 seconds, what would they say the story is about? Is that what it actually is?
- *Fix — pattern implication:* "A trail." → "A trail. Already arranged." "Footprints in snow." → "Footprints. Three sets. None of them human."
- *Fix — motif seed:* Plant a single image or sound that pays off later (a music box, a phone call, a mismatched architecture).
- *Constraint:* Visual seeds must be borrowed from elsewhere in the script, never invented during polish.

**5. Personal Anchor.** Open on a character with stakes, not on a concept, mood, or world. The character can be the protagonist or a sacrificial cold-open figure (someone we will never see again); both work. What matters is concrete personal stakes within the first 30 seconds.
- *Diagnostic:* Whose POV are we in? Do we care about them in 30 seconds? What specific detail earns the empathy?
- *Fix:* Replace generic action with specific physical detail. Not "a woman drives in a storm" — "knuckles white on the wheel, breathing too fast for the heater to keep up." Specificity = empathy speed.

### Diagnostic Pass

Score each lever ✅ / 🟡 / ❌:

1. **Lead with the Punch** — strongest beat in the first 30 seconds?
2. **Audience Implication** — does the audience know what the character does not?
3. **Imaginary World** — action verbs and concrete specifics carrying the weight?
4. **Big Promise** — can the audience name the story type in 60 seconds?
5. **Personal Anchor** — whose story is this, and do we feel them?

A 4/5 opening is strong. A 3/5 opening is functional. A 2/5 or below — restructure, do not polish.

### Hard Constraints (Polish Pass)

- Do not invent mythology not present elsewhere in the script.
- Do not relocate the protagonist's introduction without explicit writer approval.
- Do not cut sacrificial cold-open characters — they are often deliberate.
- Visual seeds for Big Promise must be borrowed from elsewhere in the script, not invented.
- If the opening already scores 4/5, only sharpen — do not restructure.
- The original opening's structural choice (cold open vs. straight protagonist intro) is the writer's call, not the polish pass's.

---

## VII. Mystery & Information Craft

> **Working draft (added 2026-05-07).** Use when the script depends on withheld information, slow reveals, embedded clues, or a buried twist — i.e. mystery, thriller, conspiracy, sci-fi reveal, character-secret drama. Sections I–V are the universal screenplay craft; Section VII layers on top when mystery is the engine. A script with no buried information can largely skip this section.

A mystery is not "a story where information is withheld." A mystery is a story where the **audience's incomplete picture of the truth** is itself the engine of attention. Every principle below exists to manage that incompleteness — keeping the audience leaning forward without cheating them, starving them, or overloading them.

### Twelve Principles

**1. The Iceberg Principle.** The audience should feel about 10% of the underlying truth at any moment. The remaining 90% is implied by what the 10% does not explain. If the visible 10% explains everything, you have no mystery — you have exposition with delay.
- *Diagnostic:* For each major mystery beat, what fraction of the underlying truth does the audience now know? If it is over 30% before the end of Act II, you are leaking.
- *Fix:* Cut explicit explanation. Replace with concrete behavior, observation, or ritual that *implies* the explanation without delivering it.

**2. Information Asymmetry Tiers.** Three levels of knowledge run in parallel: what the **audience** knows, what the **characters** know, and what the **narrator** knows (if there is one). The dramatic engine is the gap between any two tiers. Manage all three deliberately.
- *Hitchcock's bomb:* Suspense is the audience knowing more than the characters (the bomb under the table). Surprise is the audience knowing less than the characters (the bomb explodes without warning). Suspense scales with screen time; surprise spends in a single beat. Build with suspense.
- *Diagnostic:* Name the gap operating in each scene. If audience and characters are at the same tier and there is no narrator gap, the scene has no asymmetry engine — find one or cut.
- *Fix:* Withhold from the characters something the audience saw earlier. Or have the narrator (if VO/voice-of-future-self) drop a beat the present-tense characters cannot yet know.

**3. The Reveal Contract — Plant Then Pay Off.** Every payoff is paid for by an earlier plant; every plant earns its payoff. This is the single most violated rule in genre TV.
- *Map clues backwards:* Define the absolute truth of the antagonist / mystery first. Write the destination. *Then* work backwards through the script and plant the clues. Never plant forward — you will plant the wrong things.
- *Fair play:* The audience must have access to every clue the protagonist has, before the final reveal. No unearned intuition. No previously-unmentioned twins. No deus ex machina. The final twist is *surprising and inevitable* — surprising because the audience didn't assemble the picture, inevitable because all the pieces were on the table.
- *Diagnostic:* For each major reveal, find the earliest moment the clue is in the script. If the audience could not have noticed it on first watch, the plant fails. If the reveal lands without a plant, the reveal cheats.
- *Fix:* For an unsupported reveal, retro-plant the clue 1–3 acts/episodes earlier. For an unpaid plant, either pay it off or cut it.

**4. Compounding Withhold.** Each episode (or major sequence) adds **exactly one** new piece of evidence to the mystery. The audience builds the picture; you never deliver the full picture before the contracted payoff moment. Adding two pieces in one episode drains the season; adding zero starves it.
- *Diagnostic:* Per episode, what is the single new mystery piece the audience now has? If you cannot name it in one sentence, the episode is either redundant or overstuffed.
- *Fix:* Audit each episode for mystery-evidence count. Trim to one. Move surplus to the next dry episode. Promote the kept piece to load-bearing.

**5. Define the Unknowable by Negation.** When the mystery's nature is not yet revealable (because the reveal is contracted for later), define it only by what it is NOT. Negative-space definition compounds across episodes without spoiling.
- *Examples:* "They were not bound to the world the way we were." "They did not die as men do." "They simply had no idea how." "The Iron Legion was not an army."
- *Diagnostic:* If you find a sentence that explains what the mystery *is*, rewrite it as what the mystery *is not* or *does not do*. The audience will fill in the blank with their own dread.
- *Fix:* Replace any positive-definitional VO with negative-definitional VO until the contracted reveal moment. Then, and only then, reverse polarity.

**6. The Rhetorical Question as Audience Proxy.** When the audience is already on the verge of a question, voice it through the narrator. Use sparingly — once or twice per script.
- *Effect:* Converts audience confusion into shared inquiry. The audience now has a partner in not-knowing. Their attention deepens because they are no longer wondering alone.
- *Diagnostic:* Where is the audience most likely silently asking "but why?" or "what is this?" If you can find the moment, you can place the question.
- *Fix:* Insert a single rhetorical question — short, genuine wonder, not confused or panicked. Tone matters: the narrator wonders alongside the audience, never above them.

**7. Camouflage Evidence in Plain Sight (Deniable Tells).** Important clues are hidden by being mentioned casually amid other details, given double meanings, or framed as something else entirely. The audience encounters them, doesn't register them, and on rewatch sees them everywhere.
- *Patterns:* (a) **Casual mention:** the clue appears in a list of three things, sandwiched between two unimportant ones. (b) **Double meaning:** a phrase reads literally in context but reveals on rewatch. (c) **Absent detail:** the dog that didn't bark — the audience notices something is *missing*. (d) **Deniable visual tell:** an image that reads as "weird shot" first, evidence second (your sky-grid flicker, asset duplication, off-shadow on the antagonist).
- *Diagnostic:* For each major clue, can a first-time viewer plausibly explain it as nothing? If yes, the camouflage works. If no, it lands too loudly.
- *Fix:* Bury the clue inside a list. Or assign it a plausible alternative reading. Or make it literally unobtrusive (background, off-frame, brief).

**8. The Page-Turner Formula — Stakes That Force Decision.** Layer three stakes elements into every major decision the protagonist faces. Without all three, the audience drifts.
- *Time pressure:* a ticking clock or hard deadline that forecloses thinking. The protagonist cannot deliberate to safety.
- *Personal cost:* something the protagonist values — a relationship, a child, a code, an identity — is on the line of the choice. The choice has to *hurt* either way.
- *Internal + external layering:* the external goal (solve the crime, reach the valley, beat the deadline) is *physically tied* to the protagonist's internal flaw or fear. The external choice forces the internal reckoning.
- *Diagnostic:* For each major decision, can you name all three? If only two, the decision can be deferred and the audience knows it.
- *Fix:* Add the missing element. Most often the missing one is internal layering — make the external problem *also* be the protagonist's internal problem.

**9. Scene-Level Engineering — Every Scene Must Move.** Every single scene creates an emotional, informational, or relational shift. If nothing changes, the scene's gravity is zero — cut it. End scenes on hooks that make the audience need the next one.
- *End-of-scene hooks (any one):* (a) a forced decision, (b) a moment of physical danger, (c) a sudden arrival that alters direction, (d) a revealed secret, (e) a new lingering question.
- *Diagnostic:* Per scene, name the change in one sentence. If you can't, kill or fold the scene. Per scene ending, name the hook type.
- *Fix:* If a scene has no shift, find an adjacent scene whose shift can absorb it. If the scene's ending is flat, swap it for one of the five hook types — usually the lingering question is the cheapest to add.

**10. Character-Driven Red Herrings.** Misdirection must be rooted in character behavior, never random coincidence. Three subtypes — use deliberately:
- *Innocent with motive + appearance:* an innocent character has a strong reason to want the bad outcome, and is physically near the scene of it. Their innocence holds; their suspicion is real.
- *Suspicious behavior covering a different secret:* a character lies, sneaks, evades — but their secret is unrelated (an affair, a debt, protecting someone, addiction). The audience reads it as the mystery; it isn't.
- *Guilty character without apparent motive:* the actual culprit is dismissed because they have no obvious reason to do it. The audience eliminates them themselves.
- *Diagnostic:* Each red herring should withstand rewatch — the audience should see *why* they were misled, not feel cheated. If the misdirection only works because information was withheld, it's not a red herring; it's a lie.
- *Fix:* Never use coincidence as a red herring. Always anchor it in a character's contradictory but coherent behavior.

**11. Suspense Pacing — Alternate, Compress, Expand.** Suspense is built in the contrast between high-action and quiet moments, and in the deliberate stretching or shrinking of screen time relative to story time.
- *Alternation:* place terrible action immediately after a quiet or happy moment. The audience braces. The juxtaposition manufactures dread.
- *Compress dull / expand suspenseful:* summarize uneventful periods in a single sentence ("three weeks passed"). Stretch suspenseful actions across multiple beats / paragraphs / shots ("the door handle. she turns it. it does not move. she turns it again. the click of the lock against itself.") Time on the page is the audience's pulse.
- *Relentless complications:* make the protagonist's life unrelatedly hard — career collapsing, family failing, body failing — so the mystery is just one weight among many. Lessens the load-bearing demand on the central plot.
- *Diagnostic:* Every act, ask: where is the quiet that sets up the next dread? Where is the expansion that sells a single suspenseful action? Where is the compression that gets us past dull terrain?
- *Fix:* Insert a quiet moment immediately before the next reversal. Expand the next physical-suspense beat by 2–3 visible actions. Compress any sequence whose only purpose is "time passes."

**12. Act II Structural Pivots — Defeat the Saggy Middle.** Mysteries fail in Act II more than anywhere else. Two enforced pivots prevent the sag:
- *Strategic irrevocability at midpoint:* roughly halfway through, the protagonist's existing strategy must be definitively foreclosed — by a "false victory" that reveals itself as a trap, or by a setback that escalates the stakes to their highest point. The protagonist must change strategy after this beat. They cannot return to the prior approach.
- *The Whiff of Death (late Act II):* near the end of Act II, apply maximum pressure to the protagonist's *internal* flaw. Force a regression — they fail their own values, fall back to the worst version of themselves, taste their greatest fear. The audience sees the protagonist at emotional rock bottom. The Act III ascent is *only* available because they were forced this low.
- *Diagnostic:* Locate the midpoint. Is the protagonist's strategy after it the same as before? If yes, the midpoint is decorative — replace it. Locate the late-Act-II low point. Does the protagonist betray their internal flaw? If no, the climax has nothing to recover from.
- *Fix:* Engineer the midpoint as a false victory or stakes-escalation event. Engineer the late-Act-II beat as the internal failure that earns the climax's redemption.

### Diagnostic Pass

Score each lever ✅ / 🟡 / ❌:

1. **Iceberg** — does the audience feel ≤30% of the truth before Act III?
2. **Asymmetry tiers** — is the audience/character/narrator gap operating in every scene?
3. **Reveal contract** — every payoff planted, every plant paid?
4. **Compounding withhold** — exactly one new mystery piece per episode/sequence?
5. **Negative-space definition** — is the unknowable still defined by negation up to the reveal?
6. **Rhetorical question** — at most 1–2, placed where the audience is already asking?
7. **Deniable tells** — can a first-watch viewer explain them as nothing?
8. **Page-turner stakes** — time + personal + internal/external on every major decision?
9. **Scene shift** — every scene creates a change; every scene ends on a hook?
10. **Red herrings** — character-driven, not coincidence-driven, hold up on rewatch?
11. **Suspense pacing** — alternation, compression, expansion all in deliberate use?
12. **Act II pivots** — strategic irrevocability + whiff of death both operating?

A 9/12 mystery script is strong. A 7/12 is functional. A 5/12 or below — restructure the information design before polishing.

### Hard Constraints (Polish Pass)

- Do not invent reveals not present in the existing structure. Every reveal must be paid by an existing or retro-planted clue.
- Do not deliver more than one new mystery piece per polished episode without writer approval.
- Do not convert negative-space definitions to positive-space until the contracted reveal beat.
- Do not add rhetorical questions if one is already present in the same act.
- Never resolve a mystery with information the audience could not have inferred.
- Never use coincidence as the mechanism of a red herring or a reveal.
- Never explain a deniable tell in dialogue. Tells stay deniable until the contracted reveal moment.

### Reference Touchstones

- *Lost* — planting/payoff cadence; compounding withhold across multi-season arcs.
- *Westworld S1* — masterful information-tier management (audience knows what hosts don't; later, audience learns the host knows what audience didn't).
- *True Detective S1* — the dopamine ladder of Rust's monologues; suspense pacing through quiet/expansion contrast.
- *Severance* — deniable tells perfected; everything is a clue, nothing announces itself.
- *The Leftovers* — negative-space mystery taken to its limit; never explains the Departure, and is more powerful for it.
- *Gone Girl* (novel + film) — tier-flipping mid-narrative; the asymmetry inverts at the midpoint.
- *Sherlock Holmes* (Doyle's "Silver Blaze") — the absent detail (the dog that didn't bark) as the load-bearing clue.

---

## VIII. The Payoff Audit (Chekhov's Gun, Both Directions)

> **Working draft (added 2026-05-07).** A revision-pass discipline, not a generative rule. Sections I-V tell you what to write; this tells you what to cut and what to plant. Run it over a finished draft, not a blank page.

Every detail a script emphasizes creates a promise. The audience's attention system opens a loop the moment something is foregrounded - a prop held a beat too long, a name spoken twice, a scar, a phone call from an unknown number. Open loops that never close do not read as texture. They read as noise, and they teach the audience that details in this script do not matter. Once that lesson lands, they stop leaning in.

The discipline runs in **both directions**, and the second one is the failure mode screenplays actually die of.

### Direction 1 - The Unfired Gun (planted, never paid)

Something is emphasized and then abandoned. Cheap to fix: either pay it off or cut the emphasis.

**The audit question, line by line:** *what job is this doing?* A line or image earns its place if you can name the job:

- Reveals character (behavior that shows who someone is)
- Advances want (moves the POV character toward or away from the scene goal)
- Raises stakes (increases what failure costs)
- Plants a payoff (sets up something that fires later - name where)
- Establishes world (a rule or texture the story will later depend on)

If you cannot name the job, the line is decoration. Cut it. This pass typically finds more to remove than to add, which is the point - a draft gets sharper by subtraction more reliably than by addition.

### Direction 2 - The Unplanted Shot (paid off, never set up)

A payoff arrives that was never seeded. The scene "works" in isolation but reads as contrivance because the audience's prediction machine was given nothing to predict with. This is the more damaging error and the harder one to see, because the writer knows the setup exists in their head.

Symptoms:
- A solution arrives from a character or force introduced in the last ten pages
- A reveal lands with no prior clue, so the audience feels tricked rather than outsmarted
- A rescue, windfall, or coincidence resolves the climax instead of a choice

**Diagnostic:** for every major turn in Act 3, find the page number where it was planted. If there is no page number, it is not a turn. It is an intervention. Either plant it earlier or restructure so the protagonist causes the outcome.

This connects directly to the head-fake principle - a surprise lands as inevitable-in-hindsight only when the clues were there. Without them, the same beat reads as cheap.

### Running the pass

1. Read the script once marking every emphasized detail. Do not judge yet, just mark.
2. For each mark, find its payoff page. No payoff means Direction 1.
3. Read Act 3 separately. For each major turn, find its setup page. No setup means Direction 2.
4. Fix Direction 2 first. Unplanted payoffs damage a script far more than unfired guns.

### Hard Constraints (Polish Pass)

- Do not cut a plant just because its payoff is distant. Check the whole script before calling a gun unfired.
- Motifs and running images are exempt from Direction 1 when they are clearly deliberate. A recurring image is its own payoff.
- Ambiguity that is thematically intended (see Section VII on negative space) is not an unfired gun. Ask whether the non-answer is the point before cutting.
- Fixing Direction 2 usually means restructuring, which is a writer's call, not a polish pass's. Surface it, do not silently repair it.
