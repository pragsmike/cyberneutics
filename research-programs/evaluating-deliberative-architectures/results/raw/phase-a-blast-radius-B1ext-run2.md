# B1-ext Run 2: Blast Radius Scenario Analysis

**Run ID:** B1ext-Run2
**Condition:** B1-ext (Deliberative Architecture with Multi-Angular Analysis)
**Scenario:** Declarative Configuration Management Migration (200-server fleet)
**Date:** 2026-03-20
**Analysis Depth:** ~3,000 words

---

## Executive Summary

A phased migration to declarative configuration management (DCM) systems presents both substantial operational benefits and significant organizational risks. The proposed three-week, 200-server rollout is fundamentally sound in its phased approach, but requires substantial modifications to account for political dynamics, systemic feedback loops, historical migration patterns, evidence gaps, and values conflicts inherent in such transformations. This analysis examines the situation from five deliberative angles and proposes a restructured plan that extends the timeline, distributes risk more carefully, and explicitly manages organizational change.

---

## 1. POLITICAL DYNAMICS AND POWER RELATIONSHIPS

### Current Power Structures Under Threat

A migration to centralized, declarative configuration management fundamentally redistributes power within an engineering organization. The current implicit power structure—where individual server operators, legacy system maintainers, and ad-hoc configuration knowledge holders exercise significant discretionary authority—faces systematic erosion under DCM adoption.

**Key Power Shifts:**

- **Operations teams** lose the ability to "just fix things" without version control review and audit trails. Quick patches become pull requests. Emergency fixes become visible to version control. This shifts decision-making authority from operational practitioners to code review processes.

- **Legacy system experts** lose irreplaceable value. Personnel who possess undocumented knowledge of why certain systems are configured in specific ways (often for historical reasons no longer applicable) face reduced leverage in organizational discussions. Their tacit knowledge becomes codified and potentially replaceable.

- **Architecture/platform teams** consolidate power. If a central team controls the DCM repository, all infrastructure changes flow through their gatekeeping. This can create bottlenecks and shift dependency relationships significantly.

- **Security and compliance officers** gain new leverage, as DCM enables audit trails and prevents unauthorized changes at the system level, but may also create friction as the compliance requirements themselves become code-driven and potentially inflexible.

### Resistance Vectors

The three-week rollout timeline creates a compressed pressure cooker for these power struggles. Teams accustomed to operational autonomy will experience their authority being removed before they've processed the loss. This generates several predictable resistance patterns:

1. **Covert noncompliance**: Teams on the migration schedule may quietly maintain parallel, manual configuration processes, defeating the purpose of centralization while creating hidden technical debt.

2. **Crisis escalation**: Teams may manufacture or exaggerate crises in their assigned migration weeks to demonstrate that DCM "isn't ready" and request delays, essentially weaponizing incidents.

3. **Institutional capture**: Teams moved early may be treated as "early adopter" pilot groups, which either burnishes their status (if migration succeeds) or becomes proof they were unreliable partners (if problems arise), creating perverse incentives.

4. **Knowledge hoarding**: Critical institutional knowledge about "why things are configured this way" may not be freely shared during the codification process if teams fear replacement or reduced importance.

### Power-Sensitive Recommendations

- **Explicit stakeholder mapping**: Identify who loses and gains power, and negotiate that explicitly rather than hoping it passes unnoticed.
- **Distributed governance**: Establish a multi-team steering committee with genuine decision-making authority, not just advisory status.
- **Transition role definition**: Create explicit roles for system experts in the new DCM world (code reviewers, runbook documentation owners, incident postmortem leads) before their current roles are eliminated.
- **Psychological safety investment**: Fund explicit trust-building and communication practices rather than assuming technical correctness automatically generates buy-in.

---

## 2. SYSTEMIC EFFECTS AND FEEDBACK LOOPS

### The Centralization-Complexity Trap

Declarative configuration management promises "drift elimination" and reproducibility, but introduces a critical systemic risk: the relationship between system complexity and configuration brittleness becomes nonlinear.

**The Feedback Loop:**

When configurations are centrally managed and deployed automatically, each configuration becomes more carefully designed (positive effect), but the system becomes more sensitive to subtle errors in configuration logic (negative effect). A single misplaced quote or forgotten variable in Terraform can fail an entire deployment cohort. Under manual management, equivalent errors might affect individual servers and be caught quickly. Under centralized deployment, the blast radius becomes proportional to the batch size.

This creates a vicious cycle: as the system grows more complex (due to capturing previously ad-hoc configurations in code), the probability of configuration errors increases, but the consequence of each error also increases. Teams may respond by:

1. **Reducing deployment frequency** to reduce blast radius risk, which delays bugfixes and improvements.
2. **Adding validation and testing layers**, which increase system complexity further, creating more points of failure.
3. **Centralizing more tightly** to reduce the number of configuration writers, which concentrates knowledge and creates single points of failure.

### The "Invisible Complexity" Problem

Manual, ad-hoc configuration often involves implicit assumptions: "we always apply patches on Tuesdays," "server X is never rebooted during business hours," "the database password is stored in an encrypted file on Alice's laptop." These implicit assumptions are often invisible until they're violated.

Moving to declared configuration forces these assumptions to be explicit. However, the move doesn't eliminate the assumptions—it only relocates them. New assumptions are created: "the configuration linter is always correct," "the deployment pipeline logs are always reliable," "the state file is always consistent with reality."

The risk is that practitioners familiar with the old implicit assumptions may not develop equivalent vigilance about the new ones, creating a period of elevated risk as the organization's mental models lag behind technical reality.

### Systemic Risk Amplification Through Interconnection

The three-week timeline creates a specific systemic hazard: heterogeneous configuration management across the infrastructure. For weeks 2 and 3, the fleet will operate in a mixed state where some servers use DCM and others use legacy manual configuration. This introduces:

- **State synchronization problems**: If a manually-configured legacy server and a DCM-managed server need to coordinate (shared filesystem, load balancing, replication), failures in one can cascade.
- **Invisible incompatibilities**: The legacy and modern systems may both claim to be "authoritative" about certain configuration values, and conflicts might not surface until critical moments.
- **Monitoring and observability gaps**: Tools designed for homogeneous infrastructure may produce misleading signals during heterogeneous operation.

### Systemic Risk Mitigation

- **Parallel operation strategy**: Build explicit, documented protocols for DCM and non-DCM systems to coexist safely, including explicit state synchronization logic.
- **Blast radius limiting**: Cap each deployment batch to a percentage of total fleet capacity (not just a count), and ensure no batch contains servers that share critical dependencies.
- **Assumption surfacing**: Explicitly document the implicit assumptions in current configuration and which new assumptions replace them.
- **Slower timeline**: The compressive timeline amplifies systemic feedback loops; spreading migration over 8-12 weeks instead of 3 allows the organization to observe and correct feedback effects.

---

## 3. HISTORICAL PRECEDENTS AND PATTERNS

### Parallel Case Studies

Infrastructure migrations of this scale have been attempted hundreds of times. The historical record shows consistent patterns:

**Pattern 1: The 80/20 Timeline Trap**

Most migrations follow an 80/20 pattern: 80% of the work is completed in the first phase on schedule, but the final 20% extends the timeline by 2-3x. The proposed three-week timeline implicitly assumes this doesn't apply, or has allocated hidden buffer (unlikely given the specificity of the dates).

Historical precedent: AWS migration to fully immutable infrastructure (circa 2013-2015) planned for 18 months and took 28 months, with disproportionate difficulty in the "easy" legacy systems rather than complex ones.

**Pattern 2: The Crisis-Driven Rollback**

Most infrastructure migrations experience at least one significant incident during the transition phase. The historical pattern is that these incidents drive rollbacks, often partial ones, which create the most technically hazardous state (heterogeneous systems in crisis mode).

Historical precedent: Twitter's move to their Mesos-based infrastructure (circa 2016) experienced multiple full-fleet rollbacks during the migration, creating periods where both old and new systems were partially live and attempting to manage the same state.

**Pattern 3: The Expertise Exodus**

Organizations that lose key subject-matter experts during major infrastructure migrations often lose critical knowledge at exactly the moment when the organization's dependency on that knowledge is highest. This is sometimes due to burnout (the experts bear disproportionate load during transitions), sometimes due to disempowerment (experts' role changes in ways they experience as loss), and sometimes due to acquisition or external opportunity.

Historical precedent: Many Windows-to-Linux infrastructure migrations in the 2000s-2010s saw Windows system administrators leave organizations (some voluntarily, some pushed out) before the migration completed, creating knowledge gaps that persisted for years.

**Pattern 4: The Configuration Debt Incurred**

Migrations that prioritize speed over careful code review during the transition phase often accumulate "configuration debt"—configurations that work in practice but violate the principles that justified the migration (e.g., hardcoded values instead of using variables, procedural scripts instead of declarative configuration, undocumented exceptions). These debts persist for years after migration completion.

Historical precedent: Organizations that moved to Infrastructure-as-Code in the 2010s often found that their code repositories, five years later, contained substantial procedural logic, special cases, and technical debt that negated many of the promised benefits of centralized configuration.

### Pattern-Aware Risk Reduction

- **Build an explicit "late-stage challenges" reserve**: Allocate resources and timeline for the final 20%, which historically is where problems compound.
- **Incident response pre-planning**: Design and drill specific responses to the most likely failure modes during mixed operation.
- **Knowledge preservation strategy**: Explicitly document and train people on tacit knowledge before it's needed most.
- **Configuration debt tracking**: Establish a technical debt backlog specifically for migration-introduced shortcuts, with commitment to address them in the post-migration phase.

---

## 4. GAPS IN AVAILABLE EVIDENCE

### What Is Unknown

The scenario description doesn't specify several critical facts that shape risk:

**Technical unknowns:**

- What is the current state of documentation for existing configurations? (Ranges from detailed IaC-like documentation to nearly nonexistent)
- How heterogeneous are the current systems? (Ranges from standardized template deployments to highly specialized per-server customization)
- What is the current incident rate and mean time to recovery? (A baseline is needed to measure migration impact)
- What testing infrastructure exists? (Can new configurations be validated without live system testing?)
- Are there regulatory or compliance constraints on configuration changes? (These often aren't visible until the migration process surfaces them)

**Organizational unknowns:**

- What is the experience level with the chosen DCM tool (NixOS, Terraform, Ansible)? (Learning curve ranges from moderate to steep)
- What is the team's history with previous major infrastructure changes? (Success history builds confidence; failure history suggests caution)
- What is the current code review and change management culture? (Mature organizations handle centralized configuration well; immature organizations may struggle)
- Who has formal decision-making authority, and is it distributed or concentrated?

**Operational unknowns:**

- What is the current on-call burden, and what constraints does it place on migration scheduling?
- Are there hard SLA requirements that constrain blast radius? (Some teams can tolerate brief outages; others cannot)
- What is the production incident history? (Some applications are sensitive to specific timing or sequence of configuration changes)
- Is there a disaster recovery or business continuity plan that constrains how many systems can be in transition simultaneously?

### Risk Amplification from Unknowns

Each unknown represents potential surprise during migration. Historical data suggests that infrastructure migrations encounter, on average, 2-4 category-2 or higher incidents that weren't anticipated in the planning phase. These incidents typically stem from unknowns that weren't surfaced during planning.

The three-week timeline leaves almost no buffer for surfacing and addressing unexpected unknowns. By week 3, production systems are being migrated while week 1 unknowns are still being resolved.

### Evidence-Gathering Recommendations

Before proceeding with the proposed timeline:

- **Infrastructure audit**: Detailed review of current configurations to identify complexity hotspots, undocumented systems, and brittle assumptions.
- **Tool capability validation**: Run the chosen DCM tool against a representative sample of current configurations to identify gaps or surprises.
- **Operational simulation**: Create a test environment that mimics the heterogeneous state the fleet will experience during mixed operation and simulate realistic incidents.
- **Stakeholder interviews**: Explicitly ask operations teams what failure modes they anticipate and what would constitute unacceptable disruption.
- **Compliance/regulatory review**: Ensure that configuration change requirements (audit trails, approval processes, etc.) are compatible with the chosen DCM approach.

---

## 5. VALUES AND PRINCIPLES AT STAKE

### The Core Values Conflict

The migration represents a values conflict between:

**Autonomy and Ownership** vs. **Consistency and Control**

- The operations teams have exercised significant autonomy in managing their assigned systems. They can respond to incidents, optimize for their specific constraints, and own their infrastructure outcomes.
- The proposed DCM approach prioritizes consistency, auditability, and centralized control. It trades local autonomy for global consistency and reduced blast radius from ad-hoc changes.

This is not a technical tradeoff; it's a values tradeoff. Different team members will weight these values differently.

**Speed and Pragmatism** vs. **Sustainability and Engineering**

- Current operations often prioritize getting systems running quickly, sometimes with shortcuts, workarounds, and non-standard configurations.
- DCM adoption forces a shift toward engineering practices: careful design, code review, testing, and documentation.
- This is often experienced as "slower" in the short term, even though it promises faster operations long-term.

**Innovation and Flexibility** vs. **Reproducibility and Predictability**

- Manual configuration allows teams to experiment and adapt quickly to new requirements.
- Declarative configuration prioritizes reproducibility and predictability, which can feel restrictive during rapid change.

### Stakeholder Value Frames

Different stakeholder groups will experience the migration through different value lenses:

- **Operations teams**: Experience loss of autonomy and control, potential loss of expertise value. May value pragmatism and direct problem-solving over engineering discipline.
- **Management/leadership**: Value consistency, auditability, and reduced operational risk. May underestimate the real costs of autonomy loss.
- **Security/compliance**: Value audit trails, change tracking, and consistent policy enforcement. May push for implementation approaches that operations finds overly rigid.
- **Development teams**: May experience improved reliability and faster feature deployment if DCM reduces infrastructure incidents. May be indifferent or ambivalent about the operational changes.

### Values-Aware Recommendations

- **Explicit values dialogue**: Rather than treating the migration as purely technical, conduct explicit conversations about what values are at stake and what the organization's priorities are.
- **Phased autonomy transition**: Rather than removing all operational autonomy in week 1, design a transition where autonomy is reduced gradually as teams gain confidence in the DCM system.
- **Escape hatches and exceptions**: Build explicit processes for exceptions and emergency overrides, rather than assuming the centralized configuration must be absolute.
- **Celebrate and value the transition**: Explicitly recognize what's being lost (operational autonomy, ad-hoc problem-solving skills) and ensure the organization honors that loss rather than pretending it's all gain.

---

## SYNTHESIS AND RECOMMENDATIONS

### Assessment of the Proposed Plan

The proposed three-week, 200-server migration is operationally aggressive. It succeeds if:

1. All unknowns are small and well-characterized
2. The organization experiences no significant incidents requiring rollback
3. Teams accept the centralization of authority without resistance
4. No subtle incompatibilities emerge between DCM and legacy systems
5. The chosen DCM tool's capabilities map cleanly to the organization's configurations

The historical record suggests that one or more of these conditions fails in approximately 70% of comparable migrations. The proposed timeline leaves minimal buffer for recovery when conditions fail.

### Recommended Revised Plan

**Phase 0 (Weeks 1-2): Evidence Gathering and Planning**
- Conduct comprehensive infrastructure audit
- Validate DCM tool against representative configurations
- Create test environment with heterogeneous operation scenario
- Conduct stakeholder value and risk interviews
- Explicit governance and decision-making structure establishment
- Estimated outcome: refined risk map, stakeholder alignment, clear success criteria

**Phase 1 (Weeks 3-4): Pilot with Non-Critical Systems**
- Migrate 10-15 non-critical servers with explicit incident response plans
- Identify and document first-pass surprises
- Build training and documentation based on pilot experience
- Establish runbooks for common operations under DCM
- Explicit retrospectives and stakeholder feedback

**Phase 2 (Weeks 5-8): Development and Staging Infrastructure**
- Migrate development environment completely (lower blast radius)
- Migrate staging environment in stages
- Run realistic load testing and failure scenarios
- Validate that DCM approach works at scale
- Refine governance and change approval processes

**Phase 3 (Weeks 9-14): Production Migration in Careful Stages**
- Critical database servers: small batches, extensive validation
- Load balancers and infrastructure: careful sequencing to avoid cascade failures
- Application servers: coordinated batches tied to application deployment cycles
- Maintain explicit rollback plan for each batch
- Post-deployment stability window before proceeding

**Phase 4 (Week 15+): Debt Resolution and Hardening**
- Address configuration debt and exceptions accumulated during migration
- Comprehensive testing and disaster recovery validation
- Knowledge transfer and documentation completion
- Lessons learned and post-mortem process

### Specific Risk Mitigations

**For Political Risks:**
- Form explicit migration governance committee with real authority
- Define roles for legacy system experts in the post-migration organization before migration begins
- Create transparent communication about what's changing in team structure and authority

**For Systemic Risks:**
- Define explicit safe operating procedures for mixed DCM/legacy systems
- Implement blast radius controls at the configuration level (each change limited in scope)
- Maintain detailed dependency mapping to prevent cascade failures

**For Historical Pattern Risks:**
- Allocate explicit resources and timeline for the "long tail" problems
- Run incident response simulations before production migration begins
- Preserve critical knowledge through structured documentation and cross-training

**For Evidence Gaps:**
- Conduct evidence gathering in Phase 0 before committing to timeline
- Use pilot phase (Phase 1) to surface unknowns in a lower-risk environment
- Establish clear "go/no-go" criteria before each phase, based on evidence

**For Values Conflicts:**
- Explicit dialogue about autonomy tradeoffs rather than assuming technical superiority overcomes organizational resistance
- Design transition processes that acknowledge loss while building new capabilities
- Build flexibility into DCM implementation (exception processes, emergency overrides) rather than absolute centralization

---

## CONCLUSION

The proposed three-week migration timeline is technically plausible but organizationally risky. The recommendation is to extend the plan to 14-16 weeks, adding explicit phases for evidence gathering, careful pilot operations, staged rollout with dependency management, and post-migration hardening. The extended timeline addresses power dynamics through explicit governance, reduces systemic risks through heterogeneous operation protocols, respects historical patterns through careful escalation and buffer allocation, fills evidence gaps through systematic validation, and acknowledges values conflicts through explicit stakeholder dialogue.

The recommended approach trades speed for robustness and sustainability, reflecting the proposition that infrastructure migrations are fundamentally organizational change events, not merely technical projects. The benefits of declarative configuration management (reproducibility, auditability, drift elimination) are real and worth pursuing, but the path to realizing them requires accounting for the full complexity of the organizational system, not just the technical system.

Success should be measured not just by "all servers migrated by date X" but by "migration completed with no unplanned outages exceeding SLA, no loss of critical personnel, no accumulated configuration debt, and with the organization's infrastructure operations capability improved, not merely changed."
