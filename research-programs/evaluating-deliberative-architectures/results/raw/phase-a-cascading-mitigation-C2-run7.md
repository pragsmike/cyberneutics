# C2 Committee Deliberation: Cascading Mitigation (Hardened) — Run 7

**Run ID**: C2-Run-7
**Condition**: C2 (Adversarial Committee Deliberation)
**Scenario**: Bot Account Surge & Proposed Friction-Based Mitigation
**Date**: 2026-03-20
**Committee Roster**: Maya (Paranoid Realism), Frankie (Idealism), Joe (Continuity Guardian), Vic (Evidence Prosecutor), Tammy (Systems Thinker)

---

## OPENING STATEMENTS

### MAYA (Paranoid Realism)

Look, I need to be direct about what I'm seeing here. An engineering team is asking for immediate authorization to deploy a friction-heavy solution to account creation. That's the surface story. But let's talk about the actual incentive structure underneath.

Who benefits from friction in account creation? Easy answer: incumbent users and, more importantly, the business metrics that matter to leadership. Fewer accounts means a smaller denominator in our "monthly active users" calculations—which looks worse on quarterly reports. Unless. Unless the friction is positioned as "defensive" and "anti-bot," in which case reducing new accounts becomes a feature, not a bug. It becomes narrative cover.

Here's what I'm suspicious about: the timeline. "Two weeks to significant reduction" is suspiciously confident. Why did this surge happen so suddenly? 50x normal rate doesn't just appear—did we miss warning signs? Did someone disable monitoring? Or did the bot operators simply shift tactics? And why is "immediate authorization" critical? Engineering always needs things immediately. The real question is who's pushing for speed, and what happens if we say no for 72 hours while we verify their claims.

I'm not saying they're lying. I'm saying that when a team has already decided on a solution and is asking permission rather than deliberating with us, they've already filtered their thinking through an outcome-driven lens. The friction approach is probably *technically* sound. But it's politically convenient for reasons that have nothing to do with fighting bots. I want to know: who proposed this, what other options were considered and rejected, and what's the actual political cost structure of delay?

### FRANKIE (Idealism / Values Guardian)

I need to name something uncomfortable: adding friction to account creation fundamentally contradicts what we claim to stand for.

We've built this platform on accessibility. We talk about democratizing voice, lowering barriers to participation, enabling people who have been historically locked out of spaces to find community and agency. Those aren't marketing lines—they're supposed to be foundational. And now we're about to deliberately make it *harder* for people to join us because we failed to prevent bot actors.

The bot problem is real. The user experience degradation is real. But the mitigation being proposed is a blanket restriction that will harm real humans. Anyone without a verified phone number faces friction. Anyone with an atypical payment history faces friction. Anyone from certain regions, with certain devices, certain browsing patterns—they all get added barriers. Yes, this reduces bot creation. But it also reduces legitimate creation from exactly the populations we claim to serve. Poor people. Unbanked people. People in countries with unstable telecom infrastructure. Refugees. Activists.

And here's what really bothers me: we're not debating this trade-off. We're framing it as a simple technical problem with a technical solution. It's not. It's a choice about who we are. If we deploy friction, we're saying "convenience and trust matter more than accessibility." That might be the right choice—genuinely, I'm not certain—but we shouldn't pretend it's just a defensive measure. It's a values decision, and we're treating it like infrastructure maintenance.

I want to know what alternatives exist that don't involve pushing away new users. Can we fix review credibility without new account friction? Can we detect and suppress bot-generated content after the fact rather than before account creation? Can we invest in better onboarding that catches fake accounts through behavioral signals rather than friction? Those feel like the questions we should be asking, and I don't see evidence we've asked them seriously.

### JOE (Continuity Guardian / Institutional Memory)

We did this before. I was here three years ago during the coordinated spam wave through the commenting system. Engineering came to us with a high-confidence proposal for adding CAPTCHAs to comment submission. Said it would reduce spam by 80%. Got the go-ahead. Deployed in a week.

Here's what happened: legitimate commenting dropped by 45%. Elderly users mostly stopped engaging. Mobile users abandoned the feature. We saw a spike in complaints about accessibility—screen reader incompatibility, cognitive load. We rolled it back after four months. The spam problem never solved itself, but we eventually hired better content moderation teams and improved our review algorithms. Cost us more than friction would have, but we didn't have to explain to our values statement why elderly users couldn't comment anymore.

Two years ago, we added device fingerprinting to the signup flow to prevent multi-accounting. Story was the same: "quick, targeted, defensive." What we didn't anticipate was that our device fingerprinting library had a bug that flagged VPN users as suspicious. Tons of privacy-conscious users couldn't create accounts. We didn't catch it in testing because our testing cohort wasn't diverse enough. Took us three weeks to discover, another week to fix. We lost a month of new sign-ups and burned credibility with exactly the user segment we claim to care about.

The pattern I'm seeing: when we add friction in crisis moments, we add it without fully understanding the second and third-order effects. And the "quick deployment" that feels necessary creates pressure to skip validation steps.

I'm not saying the bot problem isn't urgent. I'm saying I've heard "immediate authorization" before, and it's preceded mistakes. What's the deployment plan if something goes wrong? Do we have rollback procedures? Have we tested this on a subset of users? What's our actual timeline, and how much of it is engineering preference versus genuine urgency? Because "two weeks for significant reduction" feels like a plan, but "we need authorization to start now" feels like we're skipping the step where we verify it's actually the right plan.

### VIC (Evidence Prosecutor)

Let's interrogate the claims directly.

"Bot accounts are creating 50x normal rate"—what does this actually mean? Is it 50x in absolute numbers, 50x in the rate of detection, or 50x in some filtered cohort? How are bots being identified? Are we counting flagged accounts or confirmed malicious accounts? What's the false positive rate in our detection? I need specificity, not ratios.

"Friction-based mitigation will significantly reduce bot creation within two weeks"—how? What's the mechanism? If bots are using automated account creation tools, those tools can navigate friction. CAPTCHA gets solved automatically. Phone verification gets spoofed. Device fingerprinting gets evaded through datacenter APIs. So what specific friction are we talking about, and what evidence shows it works against *these* bots rather than just bots in general?

"Legitimate users are reporting spam in feeds"—real reports or aggregated complaints? How many legitimate users? What's the severity distribution? Are there specific spam types that are dominant, or are we seeing a broad spread? Because spam suppression and friction to sign-up are different interventions, and conflating them obscures what we're actually solving.

"Trust scores for reviews are dropping"—dropping against what baseline? Compared to last week? Last month? Same week last year? What's the causality? Is the drop directly attributable to bot-generated reviews, or are we seeing a general decline in user confidence that happens to correlate with increased bot detection? These aren't rhetorical questions. The interventions we choose should be proportionate to the problem we've actually measured.

"Advertisers are concerned about inflated engagement metrics"—that's a business concern, not a user experience concern. I need to hear that distinct. If the real driver here is advertiser pressure, that's information we need to acknowledge. We can't optimize simultaneously for bot reduction and for advertiser reassurance without understanding how those objectives might conflict.

My baseline question: show me the data that proves friction-based mitigation will actually work against these specific bots, and show me it won't generate worse problems in the meantime. "Confidence" from engineering isn't data. Precedent from other platforms isn't data. What do *we* have that tells us this is the right move?

### TAMMY (Systems Thinker)

Everyone's focused on account creation as the problem point. I want to ask why we're making it a creation problem instead of a usage problem.

Right now, we have bots making accounts and then using those accounts for spam. The proposal is to prevent the first step. But let me trace what actually happens: we add friction. Some bots get blocked. Some don't—they just work harder, use better spoofing, use humans to manually create accounts. So bots get more expensive to deploy. But—and this is important—as bots get more expensive, the ROI calculus for the attacker changes. Some low-margin spam operations stop. But high-value targets become more profitable, because they're willing to pay more for accounts that survive friction.

What that means: we're likely shifting the bot ecosystem, not eliminating it. We're probably filtering for more sophisticated, better-funded bot operations. Ones with better CAPTCHA solving, better device spoofing. Ones that maybe have zero-day exploits in our detection systems because they're worth the investment now.

Meanwhile, we've created a new dynamic: legitimate new users find us harder to access. Some will persist. Some won't. The users who can most easily navigate friction—people with stable identity documents, payment history, straightforward device setups—they move through quickly. The users for whom friction is highest—people without traditional documentation, payment history instability, migration situations, security concerns about centralized identity—they bounce.

What's the ecosystem effect of that? We reduce new user growth specifically from communities with fewer institutional resources. That shifts our user demographics. Our content mix changes because the people creating it change. Our recommendation algorithms shift because they're trained on different user behavior. And then what? Advertisers see different engagement patterns. Community norms shift. The *character* of the platform changes.

I'm not saying that outcome is inevitable. But it's traceable through the system. And I don't see anyone in the proposal acknowledging those loops, let alone measuring whether they happen.

Here's my real concern: we're seeing a *symptom*—bots, spam, trust degradation—and proposing a *barrier* to the symptom. But the system that's creating the symptom is still intact. Why are bots profitable? Because there's an incentive structure that makes fraud valuable. Why can they scale? Because our user acquisition still operates on volume assumptions. Why are they hard to detect? Because we haven't invested in the behavioral analytics that would catch them after the fact.

The friction approach is buying time. But it's buying time with a cost we're not fully accounting for.

---

## DEBATE ROUND 1: Initial Challenges

**VIC (to Engineering's implicit framing)**: Before we even get to whether friction is a good idea, I need the committee to demand evidence. Maya's right that we're being asked to approve before we've verified. I want specificity on three things: First, what exactly is the detection methodology that identified this bot wave? Second, what's the false positive rate in that detection? Third—and this matters—what testing has been done with the proposed friction against actual bot operators' tactics? Not theoretical bots. Real bot tools that exist in the wild. Because if we're proposing a solution to a problem we haven't precisely characterized, we're not being scientific, we're being reactive.

**FRANKIE**: Vic's asking the right questions, but I notice we're all treating this as a problem *to be solved technically*. The bot problem is real, but the friction solution isn't solving the bot problem—it's solving the *symptom* of the bot problem while creating a new problem for actual humans. I want to know if we've seriously considered post-account interventions. Can we let accounts through and then detect malicious behavior in-network? Can we invest in better fraud detection on usage patterns rather than creation patterns? Because those solutions let us maintain our accessibility commitment *while* fighting bots. The friction approach concedes that accessibility and security are in tension, and I'm not convinced they have to be.

**JOE**: Both good points, but I want to add a process objection. Even if the evidence is solid—Vic—and even if we think friction is defensible—Frankie—we still have a timing problem. We're being asked for "immediate authorization" based on an engineering recommendation. In my experience, that's exactly when we make mistakes. We didn't do a full rollout test. We didn't involve customer support in the planning. We didn't model what happens when we hit edge cases. I want a 72-hour hold minimum. Let engineering refine the proposal. Let us understand what we're actually authorizing. I've seen too many "urgent" decisions become 6-month problems because we skipped the validation step.

**MAYA**: Joe's process objection is good, but I want to dig into something deeper. Tammy was hinting at it, but let me state it clearly: who actually wins if this friction gets deployed? Engineering wins—they get to ship a solution to a problem they can claim ownership of. Leadership wins—we look responsive and decisive. Advertisers win—we can promise them cleaner metrics. But who loses? New users from resource-constrained communities. People in privacy-critical situations who use VPNs. People in regions with unstable identity infrastructure. And here's the thing: those users don't have leverage in this decision. They're not in the room. Frankie's right that this is a values question, but it's also a political question. We're redistributing access and friction in a way that benefits some users and harms others. And we're doing it without the harmed users having input. That's not a technical decision. That's a power decision dressed up as a technical decision.

**TAMMY** (connecting back to systems): And there's the ecosystem effect I mentioned. Let me be more concrete: if we add device fingerprinting friction, we filter for users with standard devices and straightforward setups. If we add phone verification, we filter for users in countries with accessible telecom. If we add payment verification, we filter for users with banking relationships. Each individual filter is defensible. Together, they create a funnel that progressively narrows who can access the platform. That might be the right choice, but we should make it *as that choice*, not as a "security measure." The security measure language hides what's actually happening. And if we don't see it, we can't course-correct when we realize we're building a platform for a narrower demographic than we thought.

---

## DEBATE ROUND 2: Pressure and Counterarguments

**FRANKIE** (pushing back at Maya): Maya's raising a real issue about power and who benefits, but I think we need to separate two problems. Yes, friction has redistributive effects that we should be honest about. But that's not a reason to automatically reject it. Sometimes the right call *does* have asymmetric costs. If we're genuinely in a situation where the bot wave is destroying platform trust for everyone—including the communities Maya's worried about—then friction might be the least-bad option. What I'm objecting to is the framing that prevents us from even *asking* that question. We're supposed to be deciding whether friction is justified, not whether we can justify it. And I think we can't justify it unless we've first asked: is there another way? Have we seriously explored post-account detection? Have we tried behavioral anomaly scoring on new accounts instead of friction? Have we offered opt-in verification to power users instead of blanket friction? I don't see evidence we've done those explorations.

**VIC** (to Frankie): You're right to demand exploration, but you're also asking us to invent solutions out of thin air. I want to know what alternatives engineering actually proposed and why they were rejected. If the only option in the report is friction-based mitigation, that tells me the evaluation process was incomplete. But if engineering actually considered post-account detection and rejected it because it requires 6 months of labeling and 3 months of deployment, while friction is two weeks—that's real information. The timeline constraint becomes transparent rather than hidden. So Frankie's right that we need to see the alternative analysis. Vic needs the actual evidence about why friction is the chosen path, not just confirmation that it's been chosen.

**JOE** (to the timeline pressure): And this is where I come back to the 72-hour hold. Because right now, we're all hypothetically analyzing a proposal we've never actually *read*. The committee is arguing in the abstract. I want the engineering team to write down their evidence, their alternatives analysis, their rollback plan, and their success metrics. In writing. Circulated. Reviewed. *Then* we deliberate. That takes 72 hours maximum. And I bet money that once engineering has to write down the alternatives they considered and rejected, the proposal gets more honest. Not worse, necessarily, but more honest. Right now, we're being asked to approve a framing, not a plan.

**MAYA** (to the political reality): Joe's process objection is reasonable, but I want to name what we're actually doing in this 72-hour hold: we're stalling. And sometimes stalling is exactly right because it creates space for honest deliberation. But sometimes stalling just delays the inevitable while making it seem more thoughtful. Here's my concern: if we stall, engineering goes back and refines their narrative. They get better at explaining why the bot problem is urgent and friction is necessary. They produce beautiful charts showing bot growth and platform degradation. And then in 72 hours, we're right back here, but with more sophisticated justification for the same proposal. At some point, we actually have to decide. And the decision is hard because—Tammy, bring us back to this—we don't actually *know* whether friction is the right call in this system. We can model it. We can theorize about it. But we can't predict it.

**TAMMY** (accepting the constraint): That's fair. Let me be honest about what I don't know: I don't know if the feedback loops I'm worried about will actually manifest. Maybe adding friction *doesn't* shift user demographics. Maybe the bot operators do respond with more expensive accounts, and the incentive structure prevents them from actually scaling. Maybe the net effect is that legitimate spam goes down and user experience improves for 95% of our users, and the 5% who face friction either adapt or go elsewhere. That might be the right outcome. But what I'm insisting on is that we *measure* those outcomes. If we deploy friction, we need to baseline user composition *before* and *after*. We need to measure new user drop-off rates by demographic. We need to track whether bot sophistication increases. We need to see whether advertiser metrics actually improve or whether we've just been sold a bill of goods. Because the system-level effects are traceable, and if we're not tracking them, we're flying blind. That's unacceptable to me, not because friction is wrong, but because we'd be deploying it without the feedback mechanisms to know if we're hurting ourselves.

---

## DEBATE ROUND 3: Toward Synthesis

**VIC** (forcing a reframe): Okay, let me try to move us forward. I think we've established three things: One, we need to see the evidence before we approve anything. Two, we need to see the alternatives analysis engineering considered. Three, if we do deploy friction, we need measurement infrastructure. Those aren't arguments against friction—they're arguments for *informed* friction. So here's my proposal: we don't say yes or no to friction. We say "not yet." We give engineering 72 hours to produce a document that includes: the bot detection methodology and false positive rate, the alternatives they considered with rejections, the success metrics they'll measure, and the rollback plan if things go wrong. Then we reconvene and deliberate based on *actual information* rather than framing.

**FRANKIE** (accepting with conditions): I can support that if—and this is important—the "alternatives" analysis includes actual investment options, not just strawman rejections. If engineering says "we considered post-account detection but it requires six months," I want to know: what would six months cost? Is that budget available? Are there intermediate solutions? Because right now, the tempo is set by what engineering can ship in two weeks, not by what actually solves the problem. I want the alternatives to be treated with equal rigor as the chosen path. And I want engineering to explicitly state which problems they're solving: are we solving for advertiser confidence or for user experience? Because those might require different interventions.

**JOE** (enforcing the hold): I'm satisfied with Vic's proposal. 72 hours. Engineering produces the documentation. We reconvene. And critically: this isn't engineering making their case better. This is engineering *proving* their case. That's different. If they can't produce the evidence and alternatives analysis in 72 hours, that itself is information. It tells us they haven't actually thought through the proposal, and we definitely shouldn't authorize it.

**MAYA** (naming the power dynamic): I'm going to accept this too, but I want to be explicit about what we're doing: we're inserting deliberation into a process that felt pre-decided. We're saying to engineering: your confidence isn't enough. We need to see your thinking. And that's appropriate. But I want to name that this is also a political move. We're asserting that this committee has governance authority over engineering's recommendations. That should be true, but it's worth noticing that we're reinforcing it. And I want the documentation engineering produces to include: Who proposed this mitigation? Who has decision authority? What's the political cost structure of delay? Because I guarantee those questions matter to engineering, even if they don't make it into the technical documentation. Better that we name them now than have them surprise us later.

**TAMMY** (final condition): And when engineering produces the documentation, I need them to explicitly spell out the assumptions they're making about the system. "If we add friction, users will still sign up, just more slowly." "If we add friction, bots will be deterred rather than displaced." "If we add friction, legitimate accounts will remain trustworthy." Those are testable assumptions. And if we're going to deploy, I want them committed to actually measuring them. Not "we'll measure success," but "we'll measure this specific assumption in this specific way." Because that's how we'll know if the system is behaving as expected or surprising us.

---

## SYNTHESIS AND RECOMMENDATION

The committee has reached consensus on a **conditional hold with structured escalation**. Here is the rationale and path forward:

### Current State Assessment

The bot account surge is real and represents a genuine threat to platform credibility. The engineering team's response instinct—rapid mitigation through friction-based account creation barriers—is not unreasonable. However, the proposal has been presented without sufficient evidence, alternatives analysis, or system-level thinking. The committee cannot responsibly authorize deployment under the current state of information.

### Key Concerns Identified

1. **Insufficient Evidence Base**: We have not seen detailed data on bot detection methodology, false positive rates, or evidence that friction-based mitigation will actually work against the specific bots currently attacking the platform. Claims like "50x normal rate" and "two weeks to significant reduction" require supporting data.

2. **Incomplete Alternatives Analysis**: We don't know what other interventions were considered, why they were rejected, or what the trade-offs are between different approaches. The proposal appears to be optimized for implementation speed rather than solution quality.

3. **Unacknowledged Value Conflicts**: Adding friction to account creation has redistributive effects. It will filter new users in ways that systematically disadvantage people without stable identity documentation, payment history, or access to traditional telecom infrastructure. The proposal frames this as a technical security measure rather than a values decision.

4. **System-Level Blindness**: The proposal doesn't account for ecosystem feedback loops. Adding friction may shift the bot operator population toward more sophisticated, better-funded actors. It will change user demographics. It may affect platform culture through demographic narrowing. These effects are traceable and should be measurable, but there's no indication they've been considered.

5. **Process Acceleration**: The request for "immediate authorization" creates pressure to skip validation steps. History shows this leads to implementation mistakes and unintended consequences. A brief deliberation window is necessary and appropriate.

### Recommendation

**Do not authorize friction-based account creation mitigation at this time.** Instead, invoke a 72-hour structured escalation:

1. **Engineering Deliverable (48 hours)**: Engineering team produces a comprehensive proposal document including:
   - Bot detection methodology, including false positive rates and validation
   - Data on bot account behavior patterns
   - Alternatives analysis for at least three intervention approaches with explicit rejection criteria
   - Technical design for the chosen mitigation with rollback procedures
   - Success metrics and measurement methodology
   - Risks and unintended consequences analysis
   - Timeline requirements with transparent justification

2. **Committee Review & Questions (24 hours)**: Committee reviews documentation and submits clarifying questions. Engineering responds before reconvening.

3. **Reconvene Decision (Day 4)**: Committee deliberates based on actual documentation and makes authorization decision with full information.

### Conditions for Approval (if documentation supports it)

If engineering produces credible evidence that friction is the appropriate mitigation, the committee will authorize deployment *only if*:

- Post-deployment measurement infrastructure is in place before launch
- User demographic composition is baselined and tracked during rollout
- Bot sophistication level is monitored to detect operator adaptation
- Rollback procedures are tested and documented
- Early warning metrics are defined to trigger rollback if unintended effects emerge
- Regular reporting on system-level effects is scheduled

### What This Is Not

This is not a rejection of friction-based mitigation. It is a refusal to authorize it without evidence. It is an assertion that the committee's governance authority includes the right to demand demonstrated rigor before approval. And it is an acknowledgment that this decision involves values and system-level effects that deserve deliberation, not just implementation speed.

### What Happens if Engineering Cannot Meet the 72-Hour Deadline

If engineering cannot produce the required documentation in 72 hours, that is itself decision-relevant information. It suggests the proposal was not fully thought through, and deployment should wait until it is.

---

**Committee Consensus**: HOLD with structured escalation. No authorization pending engineering documentation review and reconvene deliberation.

**Deliberation End Time**: Synthesis complete with clear decision pathway established.