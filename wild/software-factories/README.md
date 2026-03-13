# Software Factories

> **Status**: DORMANT — Investigation of dark factory workflows and palgebra formalism as typed specification language. Keep in wild; clarify research direction. See [wild triage report](../../agent/archive/wild-triage-2026-03.md).

Can we build a dark factory coding agent workflow using palgebra?

NLSpecs as used by StrongDM are restricted GraphViz DOT files.
This is expressive enough to build agent pipelines.

Question: Does DOT incur limitations arising from lack of type checking and structural rigor?

Let's investigate whether palgebra formalism can help.
As a graph expression language, DOT may be isomorphic to some more tractable algebraic expression language.
We already have a functor implementation that turns palgebra into Mermaid.
Maybe we can find a functor that turns palgebra into DOT.

An aside, I think our Mermaid functor could be simplified by using simple names for the text types,
rather than insisting on displaying the (rubric, template) pair.
Just give a name to that pair.

## Contents

- **[dark-factories.md](dark-factories.md)** -- Research notes: what dark factories are, how they work, the five levels framework, open-source tooling landscape.
- **[five-levels-of-ai-coding.md](five-levels-of-ai-coding.md)** -- Summary of Nate B. Jones's video on the gap between dark factories and the rest of the industry: the METR study, J-curve adoption, org restructuring, spec quality bottleneck.
- **[palgebra-and-dark-factories.md](palgebra-and-dark-factories.md)** -- Analysis of what factory.strongdm.ai actually publishes, what happens when you naively point an agent at it, and where palgebra's distinctions (enrichment vs. transformation, soft types, catalytic resources, confidence propagation) map onto factory architecture.

## References

- [Software Factories And The Agentic Moment](https://factory.strongdm.ai/) -- StrongDM
- [Attractor](https://github.com/strongdm/attractor) -- StrongDM's open-source agent spec (NLSpecs to build your own software factory)
- [5 Levels of AI Coding](https://www.youtube.com/watch?v=bDcgHzCBgmQ) -- Nate B. Jones
- [The 5-Level Framework That Explains the AI Coding Gap](https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains) -- Nate B. Jones (companion article)
- [Simon Willison on Software Factory](https://simonwillison.net/2026/Feb/7/software-factory/)
- [Dan Shapiro: Five Levels from Spicy Autocomplete to the Software Factory](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/)
