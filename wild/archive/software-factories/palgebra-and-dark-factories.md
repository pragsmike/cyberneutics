# Can Palgebra Specify a Dark Factory?

An analysis of what StrongDM's factory.strongdm.ai actually publishes,
what happens when you naively point a coding agent at it,
and where palgebra formalism might close the gap.

---

## What factory.strongdm.ai Actually Contains

Having read the site, the published material breaks into three layers:

**Principles** describe a three-phase cycle: *Seed -> Validation harness -> Feedback loop. Tokens are the fuel.* The seed is the initial input (sentences, screenshots, existing codebase). The validation harness must be end-to-end, as close to the real environment as possible. The feedback loop samples output back into inputs, repeating until holdout scenarios pass and stay passing.

**Techniques** enumerate six patterns:

1. **Digital Twin Universe (DTU)** -- behavioral clones of third-party dependencies for deterministic, replayable validation at scale
2. **Gene Transfusion** -- moving working patterns between codebases by pointing agents at concrete exemplars
3. **The Filesystem** -- using repo navigation and file read/write as a practical memory substrate for agent context
4. **Shift Work** -- separating interactive exploration from fully-specified autonomous execution
5. **Semport** -- semantically-aware automated porting between languages/frameworks, preserving intent
6. **Pyramid Summaries** -- reversible summarization at multiple zoom levels, compressing context without losing the ability to expand

**Products** list three outputs: CXDB (context store with DAG, blob deduplication, dynamic types), StrongDM ID (federated auth for humans, workloads, and agents), and Attractor (a non-interactive coding agent structured as a graph of phases).

The critical validation constraint: code is treated analogously to an ML model snapshot -- opaque weights whose correctness is inferred exclusively from externally observable behavior. No semantic code inspection.

## What "Implement Attractor from This URL" Would Actually Produce

The dark-factories research file notes that StrongDM's repo advises telling a coding agent to implement Attractor as described by the site. This is a fascinating test case -- a Level 2 agent trying to build a Level 5 system from published materials. Here's what would likely happen:

1. **The agent scrapes the page** and extracts conceptual vocabulary -- phases, graphs, scenarios, digital twins.
2. **It confabulates an implementation** mapping those concepts onto whatever framework it knows best -- probably a Python state machine with subprocess calls to an LLM API, maybe a DAG executor.
3. **It produces something that *looks* like Attractor** -- phases, LLM calls, maybe a notion of "scenarios" -- but what it actually builds is a **narrative of Attractor**, not Attractor itself.

The irony is structural: this is exactly the failure mode the METR study identified. The output would compile. It might run. But it would be missing everything that makes the real factory work -- scenario isolation architecture, digital twin behavioral fidelity, the specific feedback loop tuning StrongDM developed over months of iteration.

The factory.strongdm.ai site is *deliberately* not a complete spec. It's a manifesto. The actual Attractor repo is three markdown files that encode the accumulated judgment of a team running this since Claude 3.5 Sonnet. Telling an agent to "implement this from the website" asks it to reverse-engineer institutional knowledge from marketing copy.

This is the brownfield problem from Nate Jones's video applied to the factory itself.

## Where Palgebra Maps Onto the Architecture

The question in the README -- can palgebra provide more structural rigor than DOT-based NLSpecs? -- gets interesting when you lay factory.strongdm.ai's architecture against palgebra's distinctions:

### Scenarios vs. Tests Are Enrichment vs. Transformation

This is the cleanest mapping. In palgebra terms:

- **Tests** entangle evaluation with implementation. They're *transformations* that can be gamed because the agent sees both input and evaluation criteria in the same context.
- **Scenarios** are *enrichments* -- they score existing behavior without modifying the artifact. The scenario suite evaluates the running software and writes to a disjoint metadata namespace (pass/fail, satisfaction fraction) without touching the code.

Enrichment's safety properties -- idempotence, parallelizability when writing to disjoint namespaces -- are exactly what make scenario isolation work. Palgebra already has formal rules for this.

### Satisfaction Is a Soft Type

StrongDM replaces boolean pass/fail with "satisfaction" -- the fraction of observed trajectories through all scenarios that likely satisfy user needs. This is soft typing: artifacts inhabit types to a degree, not boolean membership.

A palgebra-specified factory would make this explicit in YAML front matter:

```yaml
scores:
  scenario-satisfaction: 0.87
  trajectory-coverage: High
  regression-stability: Medium
```

This is just decorated text metadata. The formalism already handles it.

### Digital Twins Are Catalytic Resources

In resource equation terms, the DTU is catalytic -- it participates in validation operations without being consumed:

```
built-software x dtu-environment -> validated-software  [RunScenarios]  {catalytic: dtu-environment}
```

The twins aren't transformed by testing. They're reusable context. Palgebra's catalytic notation captures this directly.

### Confidence Propagation Applies to the Whole Pipeline

This may be the most consequential mapping. Palgebra's first propagation rule: confidence can only decrease through pipeline stages. A Medium-confidence spec cannot produce High-confidence software, no matter how many tokens you burn.

StrongDM's $1k/day/engineer benchmark makes sense through this lens -- they're not just buying compute, they're buying enough iteration to push spec quality high enough that downstream confidence remains viable. The tokens are fuel for the feedback loop that *raises spec quality*, not for brute-force generation.

### Gene Transfusion Is a Transformation Morphism with Exemplar Catalysis

```
target-codebase x exemplar-codebase -> transformed-codebase  [GeneTransfusion]  {catalytic: exemplar-codebase}
```

The exemplar isn't consumed -- it's a pattern source. The target absorbs the pattern. Provenance tracking (palgebra's second propagation rule: monotone increase) would record which exemplar contributed what, making the transfusion auditable.

### Pyramid Summaries Are Reversible Enrichments

Compression that preserves the ability to expand back to full detail is enrichment with an invertibility constraint. The text doesn't change; metadata accumulates (summary layers at different zoom levels). This is unusual -- most enrichments aren't designed to be reversible -- but palgebra's framework doesn't prohibit it. It would be a novel enrichment class worth formalizing.

## The J-Curve Applies to Methodology Too

The transcript's J-curve -- productivity dips when you bolt new tools onto old workflows -- has a direct precedent in every major methodology transition. Agile adoption followed the same shape: organizations that renamed meetings without redesigning assumptions saw things get worse. The ones that actually internalized short feedback loops eventually saw gains.

The dark factory J-curve is the same shape but the workflow delta is larger. Going from "human writes code with AI help" to "human writes specs, machine writes code" is a bigger conceptual leap than waterfall to Agile. Palgebra can't solve the people problem, but it might reduce the *specification* problem -- giving teams a rigorous language for describing what their factory should do, rather than hoping the agent infers it from a manifesto.

## What a Palgebra-Specified Factory Would Look Like

Concretely, a palgebra treatment of the dark factory pipeline might look like:

```
# Core factory loop
spec x scenario-suite -> built-software  [AgentBuild]  {catalytic: scenario-suite}
built-software x dtu-environment -> validated-software  [RunScenarios]  {catalytic: dtu-environment}
validated-software x satisfaction-rubric -> validated-software  [ScoreSatisfaction]  {catalytic: satisfaction-rubric; enriches: scores}
validated-software x threshold -> accepted + rejected  [SatisfactionGate]  {catalytic: threshold; discard: rejected}

# Feedback loop
rejected -> spec  [DiagnoseFailure]  {feedback: spec->spec}

# Gene transfusion (cross-codebase pattern transfer)
target-codebase x exemplar-codebase -> transformed-codebase  [GeneTransfusion]  {catalytic: exemplar-codebase}

# Pyramid summary (context management)
large-artifact x zoom-levels -> large-artifact  [PyramidSummarize]  {catalytic: zoom-levels; enriches: summaries}
```

This is more structurally explicit than a DOT graph: it distinguishes transformation from enrichment, marks catalytic inputs, identifies where confidence degrades, and shows the feedback loop as a typed operation rather than an implicit arrow.

Whether it's *better* than NLSpecs for directing agents is an empirical question. But it's certainly more auditable -- and auditability is what you need when the lights are off.

## Open Questions

1. **Is DOT actually isomorphic to a palgebra expression language?** The README hypothesizes this. If so, a DOT functor (parallel to the existing Mermaid functor) would let you move between representations mechanically.

2. **Can an agent bootstrap a factory from palgebra resource equations?** The equations above are more explicit than factory.strongdm.ai's narrative. Would an agent given these equations plus the techniques list produce a better Attractor implementation than one pointed at the website? Testable hypothesis.

3. **Where do human gates belong?** The factory's recursive self-assessment (scenarios evaluating scenarios) has to terminate somewhere. In palgebra terms, this is where enrichment pipelines need a human gate. The formalism should make those termination points explicit.

4. **Can the Mermaid functor be simplified?** The README notes that displaying full (rubric, template) pairs clutters diagrams. Naming the pair and displaying the name would make factory-scale diagrams readable.

## References

- [Software Factories And The Agentic Moment](https://factory.strongdm.ai/) -- StrongDM
- [Attractor](https://github.com/strongdm/attractor) -- StrongDM's open-source agent spec
- [5 Levels of AI Coding](https://www.youtube.com/watch?v=bDcgHzCBgmQ) -- Nate B. Jones
- [The 5-Level Framework That Explains the AI Coding Gap](https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains) -- Nate B. Jones (companion article)
- [Simon Willison on Software Factory](https://simonwillison.net/2026/Feb/7/software-factory/)
- [Dan Shapiro: Five Levels from Spicy Autocomplete to the Software Factory](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/)
