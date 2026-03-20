# C2 Committee Deliberation: Cascading Mitigation (Hardened) — Run 8

**Run ID:** C2-Run-8
**Condition:** C2 (Adversarial Committee)
**Scenario:** Bot Account Surge & Proposed Friction-Based Mitigation
**Date:** 2026-03-20
**Deliberation Type:** Cascading Mitigation (Hardened)

---

## Opening Statements

### Maya (Paranoid Realism)

Look, I'm troubled by the frame here. Engineering says this is "straightforward" and "defensive," and they want "immediate authorization." Those three phrases together tell me someone is trying to avoid scrutiny. Let me ask the obvious question: whose metrics improve if we add friction? The engineering team gets to claim they solved a security problem—buried under new account creation friction. Our growth team's KPIs shift. Our user acquisition cost goes up. Who absorbs that? And here's what really concerns me: the bot surge conveniently appears right when we're in a competitive squeeze with rival platforms. I'm not saying it's orchestrated, but I'm asking whether there's an incentive structure embedded in this proposal that makes friction attractive to some stakeholders regardless of whether it's the right move. The engineering team presents this as a binary—do nothing or add friction—but that's a false choice someone crafted. I need to know: Who benefits if we implement this? Who pushes back? What happens to those constituencies? Until I see that political map, I'm skeptical.

### Frankie (Idealism / Values Guardian)

This proposal cuts to the heart of who we are as a platform. We've positioned ourselves around accessibility and openness—the idea that we lower barriers to participation. We've said that explicitly in our mission. Adding friction to account creation is a direct betrayal of that positioning, regardless of how we market it. And I notice the engineering frame: "reduce bot account creation." But what we're actually doing is reducing account creation, period. Some of that reduction will be legitimate users getting frustrated and not signing up. We won't see them in the data—they'll be invisible dropouts—but they'll matter in terms of what our platform becomes. We're trading a distributed problem (spam in feeds, review trust) for a concentrated problem (fewer voices, higher barriers to entry). That's not a defensive measure. That's a values choice. And it's one that erodes the thing that made us distinctive. I'm not saying we should do nothing. But we need to own what we're doing and consider whether it aligns with the platform we claimed we wanted to be.

### Joe (Continuity Guardian / Institutional Memory)

This is almost identical to what we tried in 2023 with the email verification escalation. We added SMS verification as friction, claimed it would tank bot signups, and it did reduce automated account creation by about 40%. Everyone was optimistic. But what actually happened? First, we saw a spike in secondary verification failures—people lost access to old phone numbers, couldn't recover accounts. That cost us support tickets and churn. Second, legitimate users started gaming the system with fake verification services, which then became a new attack surface we had to defend. Third, and most insidious, the friction created an expectation that our platform was "premium" or "exclusive," which attracted a different user demographic—one with higher expectations and lower patience. We eventually had to dial it back because the cultural shift wasn't worth the bot reduction. This proposal sounds urgent because the bot surge is happening now, but urgency is exactly when we make decisions we regret. The engineering team has a two-week implementation window—that's a political choice, not a technical one. It creates pressure to commit before we've thought it through. I want to know: What's different this time that would make this succeed where 2023 didn't?

### Vic (Evidence Prosecutor)

I need data. The framing says bots are creating accounts at "50x the normal rate." What's the baseline? How many bots are actually succeeding in getting verified and remaining active? Are they being caught by downstream spam filters? How much spam are we actually seeing relative to total feed volume? The proposal talks about "significant reduction" within two weeks—what does that mean? Is it 30%? 70%? And how would we measure it? Bots adapt. If we add friction, we'll see account creation drop, but that's a proxy metric, not an outcome metric. The real question is: does platform health improve? Does trust in reviews actually stabilize? Or do bots simply shift to other attack vectors—compromising accounts through password attacks, taking over dormant accounts, using VPNs and automation to circumvent new friction? I haven't seen a threat model that says "here's why friction specifically stops this class of attacker." I've seen an assumption. And I want the engineering team to justify why two weeks is a realistic timeline for a system change that has security and UX implications they're clearly not fully thinking through. Show me the failure modes. Show me what happens when this goes wrong.

### Tammy (Systems Thinker)

I'm watching the feedback loops here, and they're concerning. Right now, the system is: bots create accounts, spam appears, users lose trust in reviews, advertisers get nervous. If we add friction, the immediate feedback is: fewer accounts created, less visible spam, advertiser confidence stabilizes, we declare victory. But the second-order effects are where things get interesting. First, friction concentrates bot creation in the hands of actors sophisticated enough to bypass it—organized operations with dedicated infrastructure. We're not eliminating bots; we're selecting for more sophisticated bots. Second, friction creates value in the secondary market—verified accounts become scarcer, so now we're incentivizing account farming and account theft as compensatory strategies. Third, we're reducing the velocity at which new legitimate users can enter the system, which changes the composition of the platform over time. We get fewer casual users, more committed users, different culture. That's not neutral. Fourth, and this is critical: if we frame the problem as "account creation friction is the lever," we're not investing in the detection and removal systems that would actually make the platform more trustworthy. We're doing cosmetic surgery while ignoring the underlying immune system. What does this do to our technical debt in moderation and abuse detection?

---

## Debate Rounds

### Round 1: Interrogating Confidence

**Vic (to Engineering's implied position):** I keep coming back to the two-week confidence. You're telling us you can implement a meaningful friction layer that stops sophisticated bot operators, and you can do it in fourteen days without security failures or UX regressions. That's either incredibly fast engineering or unrealistic confidence. Which is it? Because the 2023 verification escalation took six weeks to implement and another eight to debug. What's changed?

**Joe:** Thank you for that. This is my point exactly. In 2023, the technical team was equally confident. They had specific timelines, specific success metrics—"we'll reduce new bot accounts by 40%." They hit the technical target. But the target was wrong. The metric was gamed by secondary effects we didn't model. Why should we trust this timeline when the previous timeline was met but the outcome was misaligned?

**Maya:** And notice who's asking for immediate authorization. That's not how technical problems work. That's how political windows close. "Immediate" suggests someone has a deadline that isn't about the bot surge—it's about quarterly reporting or competitive positioning or internal stakeholder management. I want to know whose deadline this really is.

**Frankie:** I'm listening to all of this, and I keep thinking: we're making a decision about our platform's character based on urgency, not principles. We've said we're open and accessible. If that's real, it should survive a four-week timeline instead of a two-week one. The fact that "immediate" is non-negotiable suggests the decision has already been made and we're being asked to ratify it.

**Tammy:** I think the speed is actually diagnostic. If the proposal were genuine about solving the bot problem, it would include a testing phase. You'd want to pilot friction on a subset of users, measure the second-order effects, understand what happens to account farming and secondary markets. You'd want six weeks minimum. The fact that we're talking about "implementation immediately" suggests the goal isn't actually to understand the problem—it's to show decisive action. That's a systems signal. Action without feedback loops is how you end up like 2023.

---

### Round 2: The Problem Definition Trap

**Frankie:** I want to push on something fundamental. We've framed this as a bot problem, but is it really? The platform is working—spam is appearing, yes, but it's appearing in feeds, which means our feed algorithm is seeing it and not suppressing it. Our review trust system is seeing fraudulent reviews and reporting them. The system is actually detecting the problem. What if the real issue isn't the bots; it's that we haven't tuned our defenses? That we're seeing bots not because there are more, but because our detection is working? And our response is to blame account creation instead of tuning the systems we've already built?

**Vic:** That's a testable claim. How many of these bot accounts are actually being caught by downstream systems? If our content moderation catches 95% of bot-generated spam before it impacts user experience, then the account-creation friction is solving a problem our other systems have already solved. It's theater. So: show me the funnel. Where do these bot-created accounts leak through?

**Maya:** Frankie's also identifying a political dimension here. If the real problem is that our content moderation and review systems are undertuned, then the fix requires admitting those systems aren't performing as we've claimed. That's a conversation with our advertiser partners about trust metrics. That's harder than saying "we're upgrading security." Adding friction is a visible action that lets us say we took the threat seriously. Tuning detection systems is invisible. One feels like leadership; one feels like failure acknowledgment.

**Joe:** And this is exactly what happened in 2023. We added friction because account creation was a visible lever. The real problem was our downstream systems weren't mature enough to handle the attack surface we'd opened up. Rather than fix those systems, we made it harder for people to create accounts. We didn't solve the bot problem; we just made it less visible. Now, three years later, we're apparently ready to do the same thing again.

**Tammy:** This is the systems point I'm making. If bots aren't being caught by downstream systems, it's because downstream systems are the weak link. You don't fix a weak immune system by making it harder for the body to accept nutrients. You strengthen the immune system. But strengthening immune systems is slow, ongoing, requires architectural investment, and doesn't generate "quick win" narratives. Friction at signup is fast and visible. That's the feedback loop we're in.

---

### Round 3: The Legitimate User Impact

**Frankie:** I want specificity on the damage. How many legitimate users are we okay with losing if we add friction? Because we will lose some. Some percentage of people will start the signup and abandon. That's empirically true. What's our acceptable loss? 2%? 5%? And not just signup abandonment—how many existing users will be harmed by increased friction when they try to create secondary accounts for specific purposes? Artists with alt accounts, activists in sensitive regions, researchers running studies? We're designing for a threat model that probably isn't our real problem and causing collateral damage.

**Joe:** This is the invisible cost. In 2023, we never measured it directly. But we saw engagement drop 3% month-over-month in our growth cohort after friction was added. Nobody connected it to the friction. It was just attributed to "market saturation" and "changing user behavior." But the correlation was there. How many accounts did we lose? We never knew, so we never valued it correctly in the cost-benefit analysis.

**Vic:** So here's what I need from the engineering proposal: not just a bot reduction estimate, but a legitimate user impact model. What's the false positive rate on friction? How many real humans does it block or frustrate? And critically: how will we measure that? Because if we don't measure it, we'll do what we did in 2023—attribute it to other factors and never revisit the decision.

**Maya:** And this is where the political angle gets uncomfortable. Because if we can't measure legitimate user harm, then that harm is politically invisible. It doesn't show up in dashboards. It doesn't get reported to the board. Meanwhile, bot reduction is visible and gets celebrated. This creates a bias toward decisions that are politically visible even if they're net negative. I'm not saying the engineering team is consciously manipulating this. But the incentive structure is. And nobody's pushing back on it.

**Tammy:** The feedback loop problem is critical here. If we add friction and legitimate users drop, but we can't attribute it to friction, we'll never learn that this is a bad strategy. Instead, we'll keep adding friction, slowly transforming the platform from inclusive to exclusive, and attribute the transformation to "market maturation" rather than our own decisions. We're training the system to be blind to our own impact.

---

### Round 4: Synthesis Pushing Toward Recommendation

**Joe:** Let me put this directly: I don't think we should implement this proposal. Not because bots aren't a problem, but because we've tried this before and it failed. We got account creation reduction without platform health improvement. And I don't see evidence that this time will be different. The engineering team is confident in a two-week timeline. That's the same confidence they had in 2023, which was misplaced. If we're going to do this, we need at minimum: a six-week pilot on a subset of users, clear legitimate user impact measurement, and a defined rollback path if second-order effects emerge.

**Vic:** I'm with Joe on the rollback and measurement requirements. But I also need actual data before any implementation. Not projections. Not confidence. Not "we've done this before." What fraction of the bot accounts are actually generating downstream spam or review fraud? Where are the defense systems failing? Show me the threat model. Without that, we're treating a symptom without understanding the disease.

**Maya:** I want to add another condition: transparency. If we do this, we need to be honest about what we're doing and why. Not "upgrading security." "Adding friction to account creation to reduce bot accounts." And we need to be transparent about the tradeoff: fewer bots, but also fewer legitimate users, and higher barriers to entry for people without strong digital infrastructure. If we can't defend that tradeoff publicly, we shouldn't make it.

**Frankie:** I'm actually coming around slightly on this. If we're going to add friction, I want it to be minimal and reversible, and I want it to be paired with a commitment to strengthen downstream systems instead of permanently outsourcing the bot problem to signup friction. The real solution is better moderation, better review validation, better content detection. Friction buys us time to build those systems, but only if we actually build them. If we add friction and then think we're done, we've betrayed the platform.

**Tammy:** And I need to understand the second-order effects we're not seeing. If we add friction, what happens to the secondary market in verified accounts? Do we start seeing account farming and account theft as compensatory strategies? How do we detect that? And what happens to platform culture? Do we become more exclusive? Do we lose the casual-user constituency that made us distinctive? This can't be a one-time implementation. This is a multi-month observation and adjustment cycle.

---

## Synthesis and Recommendation

### Summary of Debate

The committee deliberation surfaced significant concerns about the proposed friction-based mitigation despite its apparent simplicity:

1. **Institutional Memory**: Past attempts (2023) to add friction to account creation succeeded as a metric (bot reduction) but failed as strategy (secondary effects, security debt, platform culture shift). No material evidence that current circumstances differ.

2. **Evidence Gaps**: The proposal lacks threat modeling, legitimate user impact estimates, and a clear understanding of where downstream detection systems are failing. Bot account count is confused with bot-generated harm. No measurement of the actual problem being solved.

3. **Political Incentives**: The two-week urgency timeline is politically diagnostic, not technically justified. Speed creates bias toward visible action (friction) over invisible strength (detection systems). Legitimate user harm will be invisible in metrics and thus undervalued.

4. **Values Conflict**: The proposal directly contradicts stated platform positioning around accessibility and openness. The committee recognized this as a deliberate choice with cultural consequences, not a neutral defensive measure.

5. **Systems Risk**: Adding friction at signup concentrates bot creation in the hands of sophisticated operators, potentially creates secondary-market incentives (account farming, theft), and reduces platform's ability to build immune-system-strength (detection, moderation). One-time implementation without feedback cycles perpetuates blindness to second-order effects.

---

### Recommendation: Conditional Proceeding with Major Modifications

**The committee recommends against the proposed two-week implementation timeline. However, we recommend a modified approach that addresses the underlying platform health problem while avoiding the institutional and values risks identified:**

#### Immediate Actions (Week 1-2):
1. **Conduct threat characterization**: Measure what fraction of bot accounts create actual user-facing harm (spam, fraudulent reviews, engagement manipulation). Separate bot-account-creation rate from bot-harm-impact. This determines whether account creation friction is solving the right problem.

2. **Audit downstream detection systems**: Map why bots are succeeding past content moderation, review validation, and feed filtering. Identify specific gaps. This provides evidence for whether friction or detection-strengthening is the appropriate lever.

3. **Establish baseline metrics**: Measure current legitimate user account creation friction and abandonment rates. This is the baseline against which we'll measure any new friction's impact.

#### Medium-term Approach (Week 3-8):
1. **Pilot friction on subset**: If threat characterization confirms that bot accounts are causing material harm AND that harm isn't being caught downstream, pilot friction on 5-10% of signup flows. Measure specifically:
   - Bot account reduction rate
   - Legitimate user abandonment rate
   - Secondary account-creation patterns (are real users finding workarounds?)
   - Secondary market emergence (are verified accounts being traded?)
   - Detection system performance changes

2. **Parallel: Strengthen detection systems**: Run simultaneous investment in review validation, content moderation, and abuse detection. Even if friction is necessary, it's a temporary lever. Long-term platform health requires stronger immune systems.

3. **Publish findings weekly**: Make the measurement visible to stakeholders (including external partners who depend on platform openness). Reduce political invisibility of impacts.

#### Decision Threshold (Week 8):
- If legitimate user abandonment exceeds 2%, or if secondary markets for verified accounts emerge, or if downstream detection improvements prove sufficient, rollback friction completely.
- If friction reduces bot harm by >50% with <1% legitimate user impact, consider graduated expansion (not immediate platform-wide implementation).
- If friction is working but secondary effects are emerging, design countermeasures before expansion.

---

### Political Context

The committee recognizes that the two-week authorization request is likely driven by:
- Advertiser pressure for visibility that platform is "taking action"
- Competitive positioning ("we're more secure than rivals")
- Internal stakeholder alignment (certain teams benefit from friction more than others)

**We recommend decoupling timeline from authenticity.** A seven-week pilot with clear measurement is visible action. A two-week implementation followed by six months of regretting secondary effects is hidden failure. The organization should communicate clearly to external stakeholders that we're addressing bot problems with evidence-based rigor, not speed theater.

---

### Values Clarity

The committee recommends the organization make an explicit values choice:
- **If accessibility and openness are genuine platform values**: friction is a temporary measure paired with detection system strengthening, not a permanent solution.
- **If the platform is shifting toward premium/exclusive positioning**: own that choice, communicate it, and recognize the cultural consequences.

Do not dress friction-based exclusion in the language of security and openness.

---

### Final Assessment

**Proceed with the modified approach, not the proposed approach.** The modified approach:
- Addresses the underlying bot problem through evidence (threat characterization)
- Tests the proposed friction with measurement and rollback conditions
- Builds long-term platform health through detection systems rather than permanent barriers
- Maintains institutional alignment with stated values
- Learns from institutional memory (2023) rather than repeating it

The organization can show decisive action without sacrificing rigor or values clarity.

