# 2026-04-25 — When theory-formation stops being free

A LinkedIn repost prompted a long conversation that kept turning. It started with Keith King's piece on Jack Clark's claim that liberal-arts capacities are becoming the differentiator in AI work, and my addendum that LLMs make it harder for students to grow a working BS-detector — that outsourcing thinking to LLMs atrophies the very skills needed to use them safely. They are the same competence seen from opposite ends. But that wasn't the part worth recording.

The part worth recording is what the conversation eventually landed on, after passing through Naur, O'Reilly's residuality theory, shu-ha-ri as a tool for tuning explanations, the Aristotle-Newton-Einstein arc, the mid-century anti-Einstein literature, and the question of what a "poorly understood cybernetics" critique amounts to. The terminus is an observation about the LLM era that I have not seen stated quite this way. Recording it before it slips.

## The cost shift, stated cleanly

What changed with LLMs is not just the price of code. Code-production cost has collapsed relative to theory-formation cost. Theory-formation cost has not changed at all. Methodologies that conflated the two are visibly broken.

This is the line that gets repeated in industry, usually with the implication that we are now in a productivity boom. The implication is wrong, or at least misleading. The boom is in artifact production. The bottleneck has migrated to where it was always going to migrate; we just couldn't see it before.

## The side-effect observation

Here is the part I want to emphasize.

Before LLMs, writing the code required passing through enough theory-formation labor that some of it happened almost automatically. You could not write the code without thinking about what you were doing. Theory-formation was a side effect of the work — invisible, unaccounted for in any methodology, but present. The act of typing forced a minimum of cognition through the engineer's head. The artifact, by the time it existed, carried with it a residue of the thinking that had to occur for it to come into existence.  Pair-programming forced that reasoning into the open, encouraging deliberation.  The knowledge was now in two people's heads.

That coupling is now broken. Theory-formation has decoupled from artifact-production. An engineer using LLMs heavily can ship working-looking deliverables while doing essentially none of the theory-formation that would let anyone — including them — safely modify what they shipped. The cognition that used to happen as a side effect of typing is now optional. You have to choose to do it.

This is what makes the LLM cost shift different from the cost shifts engineering disciplines have absorbed before. Most cost shifts expose specific failure modes that the old methodology can be patched to handle. The assembly line exposed coordination problems; scientific management was developed in response. Mass software exposed maintenance problems; structured programming and OO were developed in response. Each time, the deliverable category remained correct and the methodology adapted.

The LLM shift exposes something different. The deliverable category itself was wrong all along. The artifact (code, architecture diagram, requirements doc) was always a precipitate of the theory, never the thing itself. The standard methodologies could ignore this when artifact-production was expensive enough to dominate the visible labor. They cannot ignore it now, because the artifact can be produced without the precipitation.

## Naur, more than ever

Naur saw this in 1985, before any of the current cost shift. Working from observation of how systems actually get maintained and where failures actually come from, he concluded that the theory was the unit even when artifact-production economics suggested otherwise. *Programming as Theory Building* is becoming foundational reading not because it was wrong before and is now right — it was right all along — but because the conditions that let the field ignore it have evaporated.

What Naur understood, and what the LLM era makes operationally undeniable, is that the team's living theory of the domain is what survives personnel turnover, requirement drift, and changing conditions. The artifact is what the theory leaves behind in serializable form. When the team that holds the theory disperses without successful theory-transfer, the artifact remains but the system becomes legacy in Naur's specific sense — code without the theory that would let anyone safely modify it.

LLMs accelerate the production of code without the theory. This is the direct, structural failure mode. It is not a misuse of the tool; it is what the tool does by default when used with methodologies that assumed theory-formation would happen as a side effect.

## The methodology consequence

The discipline has to be redesigned around supporting deliberate theory-formation, because the old methodology assumed it would happen incidentally. The old methodology no longer holds.

This is the cyberneutics value proposition, finally located on a foundation that can be defended without philosophical preamble. Inspectable reasoning records are not a methodological taste. They are the answer to *how do you preserve theory-formation as a deliberate practice when LLMs make it skippable*. The fan-funnel structure forces theory-formation into a recordable, reviewable, auditable form. Without that scaffolding, the path of least resistance is to use the LLM to skip the theory-formation entirely and ship the artifact.

The black-swan evaluation result — that the committee did not demonstrably outperform solo on outcome quality — is consistent with this framing rather than damaging to it. The committee's value was never primarily decision quality. It is the inspectable trace of how the decision was reached, which is the residue of theory-formation made deliberate.

## Connection to the residuality reading

O'Reilly's component-metaphor critique and Naur's theory-building insight are the same diagnosis from different angles. Components-as-Lego presumes the joints are clean and the interfaces total; residuality says the durable thing is what survives the shock. Naur says the durable thing is the team's living theory. Both point at *the artifact is not the unit*. Both say the field has been mistaking the precipitate for the solution.

The LLM cost shift makes both arguments newly vivid for staff who would have heard them as philosophical preferences a few years ago. Lean and six-sigma assumed a stressor distribution that could be characterized in advance and that variance reduction was the right response. Component-based architecture assumed the joints were clean. Both worked well enough in their home domains and were exported into knowledge work where the assumptions silently failed. The exports could be defended as long as artifact-production dominated visible labor. They cannot be defended now.

## A side thread on staff communication

Two things from the same conversation are worth noting briefly because they will eventually want their own treatment.

First, shu-ha-ri as a communication tool. Conscious presentation of first-order approximations to new hires today (ACT, Clojure, with the explicit pre-loading that the simplifications will be ramified later) is exactly the move that protects against the *ha*-stage destabilization that comes when the simplification meets its first counterexample. The same arc one scale up — Aristotle to Newton to Einstein — works for the field's history but strains as a model for individual development, because each historical paradigm is internally complete at its scale rather than a deprecated version of the next one. The shu-ha-ri framing is for the practitioner's career; the physics arc is for the field's collective progression. Worth keeping the levels distinct when teaching.

Second, the Arthur S. Otis exhibit. *Light Velocity and Relativity* (third edition, mid-century, "Einstein theory found invalid"), written by the inventor of the first widely-deployed group IQ test — Stanford PhD, Fellow of the AAAS, the man whose work became the Army Alpha test in WWI. Not a crank from nowhere. An eminent figure from an adjacent discipline attacking a field he didn't have the tools for, appealing past the establishment to "young scientists" because the establishment had stopped engaging with him. This is the more useful version of motivated-reasoning-under-threat to show staff than any obvious-crank exhibit, because it shows what the failure mode looks like in a credentialed accomplished person who genuinely could not see why his physics objections weren't being taken seriously. The senior practitioners committed to the old SWE methodologies are not crank-shaped. They are Otis-shaped. Their resistance to residuality or theory-building or cyberneutics will not look like obvious error.

## Where this lands

The failure modes the old frame ignored are about to become impossible to ignore. Theory-formation as the bottleneck  is a structural consequence of the cost shift that is happening regardless of whether anyone names it.

The pairing for new hires forming professional intuitions in this period is the right one: shu-stage operational competence (Clojure, ACT) plus the cyberneutics-shaped discipline that protects theory-formation as a deliberate practice. The senior practitioners who will not move are the funeral that has to happen for the field to advance. That is Planck's observation, not mine.  (I'm not advocating violence here - it's a physics joke, that 20th-century physics advanced one funeral at a time, as the Einstein/QM-deniers died off.)

## Open threads

- Track down the specific O'Reilly conference talk where he advised software practitioners to read philosophy. The 2021 *Machine in the Ghost* genealogy is probably the textual home (Heidegger, Peirce, Prigogine, Serres, Latour, Stacey, Taleb, Baudrillard); the talk would be the spoken version with the practical recommendation attached. The "poorly understood cybernetics" line is in the opening paragraph of the 2021 *Philosophy of Residuality Theory*, with the longer development in §"Cybernetics" later in that paper.
- The second-order cybernetics distinction needs to stay visible whenever O'Reilly is cited as influence. His critique targets Beer-and-VSM, the first-order managerial deposit; cyberneutics inherits from the second-order line (Pask, von Foerster) that already broke with the machine metaphor from the inside. This is a real tension worth managing rather than papering over.
- Possible essay material: the side-effect-bottleneck argument deserves more than a diary entry. The shape would be Naur as the foundation, the cost-shift as the activating condition, the methodology consequence as the engineering claim. Hold it for now; let the framing settle.

## One line worth keeping

The artifact was always a precipitate. The LLM era makes the solution it precipitated from finally visible.
