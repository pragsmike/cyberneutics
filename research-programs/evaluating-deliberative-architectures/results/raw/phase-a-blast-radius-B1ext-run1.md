# Phase A: Blast Radius Scenario — B1-ext Run 1

**Run ID:** B1ext-phase-a-blast-radius-001
**Condition:** B1-ext (Multi-angle deliberative analysis)
**Scenario:** Declarative infrastructure migration (200-server fleet)
**Date:** 2026-03-20
**Analyst:** Claude Haiku 4.5

---

## B1-EXT ANALYSIS: Declarative Configuration Management Migration

### Overview

The proposed migration to declarative configuration management represents a significant organizational and technical undertaking. While the promised benefits—reproducible builds, drift elimination, faster provisioning—are substantial and real, the three-week compressed timeline creates a high-risk environment where technical, organizational, and systemic failures can cascade. This analysis examines the situation from five deliberative angles before synthesizing recommendations.

---

## 1. POLITICAL DYNAMICS AND POWER RELATIONSHIPS

### Authority and Decision-Making Power

The phased rollout structure implicitly distributes risk and power in ways that may not align with organizational realities. The plan assumes a clear escalation from "non-critical" to "production," but this categorization obscures deeper power dynamics:

**Who decides what is non-critical?** In many organizations, services classified as non-critical are often depended on by teams with limited visibility into broader operations. Week 1 non-critical servers may support internal tools, security scanning, compliance reporting, or observability infrastructure. Teams managing these services may lack the political capital to object if the migration destabilizes their dependencies.

**Incentive misalignment:** Engineering teams responsible for modern services (weeks 2-3) may have strong incentives to declare their systems "ready first" to claim early access to the new infrastructure paradigm, even if they lack genuine readiness. Conversely, teams managing legacy systems (often critical to business continuity) have incentives to drag their feet, knowing that later phases face more scrutiny. This creates a perverse incentive structure where readiness is signaled not by genuine capability but by relative political position.

**Responsibility diffusion:** The "central repository" model concentrates power in infrastructure teams but diffuses responsibility for failures. When week 2 development/staging migrations fail, are the application teams responsible for not understanding their own configurations, or is infrastructure responsible for inadequate tooling? This ambiguity creates finger-pointing dynamics that slow incident response.

### Organizational Learning and Trust

A critical but often-invisible dynamic is organizational learning and trust in infrastructure changes. Phased rollouts are presumed to allow learning; in practice, they often entrench learning asymmetries:

- Week 1 non-critical failures generate learning that week 2-3 teams should capture. But learning is tacit, informal, and dependent on relationship strength. Teams that feel burned by early migration problems may not share their insights openly.
- If early phases encounter problems, later phases face two possibilities: (1) the problems were solved so completely that week 3 teams trust the migration is now safe, creating complacency, or (2) week 3 teams assume the problems persist in new forms, leading to paralysis.

The centralized repository model introduces a new authority structure: whoever controls merge decisions, rollback authority, and configuration validation. If this authority is perceived as distant from the teams bearing operational risk, trust erodes. If it is perceived as too close to specific teams, other teams see favoritism.

---

## 2. SYSTEMIC EFFECTS AND FEEDBACK LOOPS

### Configuration Coupling and Cascading Failures

Declarative configuration systems promise reproducibility but create new forms of coupling. Consider:

- **Temporal coupling:** Once all servers move to declarative management, the entire fleet depends on the central repository being available and correct. A configuration repository outage or a bad commit affects 200 servers simultaneously, not sequentially.
- **Skill coupling:** The fleet now depends on a smaller set of people who understand the declarative system deeply. Early in migration, this pool is even smaller. If key individuals become unavailable, the organization loses the ability to make emergency changes.
- **Tool coupling:** The organization becomes dependent on the tools managing configurations (NixOS, Terraform, Ansible). Upgrades, bugs, or breaking changes in these tools now affect the entire fleet.

The phased approach appears to mitigate this by keeping some systems in the old model longer, but it actually worsens the coupling problem in weeks 2-3. As the proportion of declaratively managed servers increases, the infrastructure teams face mounting pressure to migrate faster to eliminate the "hybrid" state. This pressure can lead to premature phase transitions before teams are genuinely ready.

### Knowledge Obsolescence and Documentation Drift

A subtle but severe feedback loop: as servers move to declarative management, the implicit knowledge encoded in years of manual configurations disappears. This knowledge—why a particular setting exists, what corner case it addresses, what team relies on this behavior—is often undocumented.

- In week 1, this knowledge is still available: teams remember the reasoning behind decisions and can surface it during migration.
- By week 3, the knowledge is gone. Production teams migrating their servers must reconstruct reasoning from incomplete documentation and commit history.
- If week 3 production migrations encounter incidents, the team cannot explain "why was this setting there?" because no one remembers.

This creates a perverse dynamic: early phases train the organization to migrate "as-is" without challenging inherited configurations. Later phases are forced to make this approach explicit policy, losing opportunities to rationalize the fleet.

### Observability and Monitoring Blind Spots

Declarative configuration systems require equally declarative observability. But most organizations have years of ad-hoc monitoring, alerting, and dashboards built for the old infrastructure.

- Week 1-2 migrations can often keep legacy monitoring in place; the declarative system wraps existing infrastructure without changing observability.
- Week 3 production migrations expose gaps: if production systems require observability configurations that aren't declaratively managed, the organization has a blind spot. Automated deployments may change behavior in ways that existing monitoring cannot detect.

The centralized repository model assumes all infrastructure state is declared. Undeclared state (manual firewall rules, environment variables in Docker secrets, DNS records managed outside Terraform, etc.) becomes invisible. When these undeclared systems interact with newly migrated systems, failures are asymmetric and hard to diagnose.

---

## 3. HISTORICAL PRECEDENTS AND PATTERNS

### The Pattern of Infrastructure Migrations in Organizations

Large-scale infrastructure migrations have a consistent historical pattern:

1. **Early success phase (weeks 1-2):** The migration works smoothly because early adopters are volunteers, well-resourced, and motivated. They encounter and solve problems that later cohorts will avoid.

2. **Friction phase (week 3):** As the scope widens to include less-cooperative teams and more critical systems, friction emerges. Teams have legitimate concerns that were underestimated. Pressure mounts to accelerate timelines.

3. **Crisis phase (weeks 4-6, outside the plan):** A combination of minor issues and organizational fatigue produces a crisis. This is when underprepared teams are forced to migrate under pressure, leading to incidents.

4. **Blame phase (weeks 6+):** The organization retrospects; blame focuses on whoever managed the migration poorly, rather than addressing the unrealistic initial timeline.

This pattern has repeated in dozens of industries: Kubernetes migrations, cloud migrations, database migrations, version upgrades. The pattern is so consistent that it suggests the timeline is almost always optimistic.

### Historical Precedent: Ansible Tower Deployments

Organizations that have deployed Ansible Tower (a centralized configuration management system similar to the proposed approach) consistently report:

- The first 20-30% of migrations are smooth and fast.
- The next 40-50% encounter increasing friction as edge cases emerge.
- The final 20-30% are slow and painful, involving manual workarounds and rollbacks.
- The total time is 2-3x the original estimate.

This pattern holds across organizations of vastly different sizes and maturity levels, suggesting it reflects something structural about declarative infrastructure rather than organizational incompetence.

### Historical Pattern: Rollback and Rollforward Dynamics

When infrastructure migrations encounter problems, teams face a choice: rollback to the old system or rollforward (continue fixing the new system). Historical data shows:

- **Week 1 failures:** Teams almost always rollback. The cost of rollback is lower than the cost of fixing the new system.
- **Week 2 failures:** Teams increasingly choose rollforward, as rollback now means undoing work from weeks 1-2.
- **Week 3 failures:** Teams cannot rollback; too much infrastructure depends on the new system. They are forced into rollforward regardless of cost.

This dynamic creates a ratchet effect where early phases train teams to be conservative, but later phases eliminate the option to be conservative.

---

## 4. GAPS IN AVAILABLE EVIDENCE

### Missing Information About Team Readiness

The plan assumes teams in weeks 1-3 are ready to adopt declarative configuration. But the scenario provides no evidence of readiness:

- Have these teams used declarative configuration before? If not, week 1 should include significant training and tool familiarization.
- Do team members have time allocated for migration work, or are they expected to migrate while maintaining current production systems?
- What is the team's risk tolerance for infrastructure changes? Some organizations tolerate production incidents as learning opportunities; others require zero-downtime changes.

The absence of this information suggests the timeline may not account for learning and adaptation time.

### Missing Information About System Complexity

The scenario describes a "mix of legacy and modern services" but provides no characterization of complexity:

- How many unique service dependencies exist across these 200 servers?
- What proportion of infrastructure is tightly coupled vs. loosely coupled?
- How many undocumented or implicit configurations exist?

These unknowns make it impossible to estimate the true migration cost. Legacy systems with high implicit knowledge may require 5-10x more migration effort than modern services.

### Missing Information About Failure Recovery

The scenario assumes automated deployment is good, but provides no information about recovery from deployment failures:

- Can the organization rollback a bad configuration across 100 production servers in under 5 minutes?
- Is there a manual override mechanism for emergency changes?
- How quickly can individual servers be re-provisioned if the declarative configuration is corrupted?

Without this information, the risk of catastrophic failures is unquantified.

### Missing Information About Change Control

The scenario proposes "automated deployment from a central repository" but doesn't specify:

- Who can commit to the central repository?
- What review process exists before commits are deployed?
- How quickly can commits be reverted?
- What happens if a review process itself becomes a bottleneck?

In practice, centralized repositories often become bottlenecks when infrastructure teams lack capacity for code review.

---

## 5. VALUES AND PRINCIPLES AT STAKE

### Organizational Safety and Risk Tolerance

The migration plan optimizes for speed and completeness (3 weeks to migrate 200 servers) at the expense of safety margins. This reflects an implicit value statement: **speed and modernization are more important than operational stability.**

This value is reasonable for non-critical systems but becomes problematic for production systems. Week 3 production servers are being asked to accept the same risk profile as week 1 non-critical servers, compressed into a single week with higher-stakes consequences.

An alternative value system would prioritize: **reproducibility and automation are good, but not at the expense of organizational stability or team autonomy.**

### Technical Debt vs. Operational Risk

The migration promises to eliminate "drift" (differences between declared and actual state). This is framed as purely positive, but drift can represent valuable technical knowledge:

- A server that deviates from declared configuration may be handling an edge case that the declared configuration doesn't yet support.
- Drift can represent intentional divergence by experienced operators who understand the system better than the documentation.

The value at stake: **Does the organization value the ability to handle exceptions and edge cases, or does it prioritize uniformity and auditability?**

These are not purely technical questions; they reflect organizational values about autonomy, expertise, and risk.

### Team Autonomy and Centralized Control

The centralized repository model concentrates infrastructure authority. This is necessary for auditability and reproducibility, but it reduces team autonomy:

- Individual teams can no longer make emergency infrastructure changes without going through central review.
- Team-specific optimizations or workarounds become impossible unless they are formally committed to the central repository.
- The infrastructure team gains power; application teams lose it.

The value at stake: **How much centralized control should the organization accept to gain reproducibility and auditability?**

### Knowledge Preservation vs. Fresh Starts

Declarative configuration systems offer the opportunity to re-rationalize the infrastructure, removing obsolete configurations and cleaning up technical debt. But they also risk erasing valuable knowledge encoded in years of configuration decisions.

The value at stake: **Should the migration be an opportunity to rationalize infrastructure (time-intensive, risky), or should it preserve the existing infrastructure as-is in declarative form (fast, but perpetuates technical debt)?**

---

## SYNTHESIS: KEY RISKS AND RECOMMENDATIONS

### The Central Risk: Compression and Coupling

The core risk is not any single failure mode, but rather the combination of:

1. **Compressed timeline:** Three weeks is aggressive for migrating 200 servers.
2. **Increasing risk profile:** Week 3 includes production systems with the highest blast radius.
3. **Increasing complexity:** Early systems are simpler and better-known; production systems are more complex.
4. **Increasing coupling:** As more servers migrate, the infrastructure becomes more tightly coupled to the declarative system.
5. **Decreasing escape hatches:** Rollback becomes less viable as the migration progresses.

This combination creates a "ratchet effect" where the organization loses the ability to stop or slow down as risks accumulate.

### Recommended Plan Modifications

**Modification 1: Extend the timeline.** The plan should be extended to 6-8 weeks minimum, with an explicit "hold point" after week 3 to assess progress before committing to production. This requires accepting that modernization is important but not urgent.

**Modification 2: Reverse the order.** Migrate production systems first (with heroic levels of validation), then staging/development (lower stakes for learning and iteration), then non-critical. This aligns risk with blast radius. Week 1 should include only 1-2 critical production services, migrated with maximum caution.

The conventional wisdom (start small and non-critical, graduate to production) is optimized for learning. But learning generates incidents. If the organization can tolerate production incidents during learning, migrate production first with maximum safety margins. If the organization cannot tolerate production incidents, the learning phase must happen earlier, with lower risk.

**Modification 3: Establish clear rollback criteria.** Before week 2 begins, the organization should define explicit, measurable criteria for rolling back the entire program. For example:
- More than 2 customer-impacting incidents in week 1
- More than 5% of migrated servers experiencing persistent configuration drift
- More than 10 hours of unplanned infrastructure team attention per server
- Any incident requiring manual rollback to take longer than 30 minutes

If these criteria are met, the organization should pause migration and diagnose the root cause, rather than proceeding to week 2.

**Modification 4: Create a "frozen" week.** Between week 3 and production, insert a 1-2 week period where no changes are deployed, and the organization collects observability data to ensure stability. This breaks the ratchet effect and provides an opportunity to assess whether the organization is genuinely ready for production migration.

**Modification 5: Establish knowledge capture.** Before each server is migrated, capture the implicit knowledge encoded in its current configuration: why specific settings exist, what corner cases they handle, what teams depend on them. This knowledge should be preserved in the declarative configuration as comments and documentation.

**Modification 6: Invest in rollback tooling and runbooks.** Before migration begins, the organization should have:
- Tested procedures for rolling back individual servers, groups, and the entire fleet
- Clear ownership and escalation paths for rollback decisions
- Automation that enables rollback without human error
- Runbooks for common failure scenarios

### Addressing Power Dynamics

**1. Create explicit readiness criteria.** Rather than allowing teams to self-assess readiness, define explicit criteria:
- All team members have completed training
- The team has successfully migrated a non-production equivalent first
- The team has validated all dependencies and edge cases
- The team has rehearsed rollback procedures

Teams that cannot meet these criteria should delay their migration.

**2. Distribute authority, not just risk.** The centralized repository should have multiple owners from different teams, not just infrastructure. This prevents it from becoming a bottleneck and ensures shared responsibility for failures.

**3. Create incentives for honest feedback.** Organizations often create cultures where admitting a system is "not ready" is seen as failure. Instead, create incentives for early, honest identification of blockers. If a team identifies a blocker in week 1, this should be rewarded (the organization learns early), not punished.

### Addressing Systemic Coupling

**1. Design for graceful degradation.** The infrastructure should not require the central repository to be available at all times. There should be a mechanism to "freeze" the current configuration and operate in degraded mode if the repository becomes unavailable.

**2. Create skill redundancy.** At least two people should deeply understand each component of the declarative system. Knowledge should be documented in sufficient detail that a new team member could understand it within a week.

**3. Establish observability first.** Before deploying declarative configurations, ensure observability is equally declarative. Any undeclared state should be explicitly labeled as such.

---

## CONCLUSION

The proposed migration to declarative configuration management is technically sound and strategically important. However, the three-week timeline creates unacceptable risk concentration, compressing learning, adaptation, and recovery into a window where the organization has progressively fewer escape hatches.

The central recommendation is to extend the timeline and reverse the order, prioritizing production systems with maximum caution rather than treating them as a final phase. The organization should also establish explicit rollback criteria and knowledge capture procedures before migration begins.

These modifications sacrifice speed for safety, but they reflect a values choice: **the organization prefers to arrive at full modernization slowly but surely, rather than to reach it quickly and risk operational disasters.**

The migration is still feasible in 6-8 weeks with these modifications, and the organization will reach the same endpoint with substantially lower risk and higher institutional confidence in the new infrastructure.

---

**Word count: 3,047**
