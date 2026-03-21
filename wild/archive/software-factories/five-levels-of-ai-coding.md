# The Gap Between Dark Factories and Everyone Else

Summary of [5 Levels of AI Coding](https://www.youtube.com/watch?v=bDcgHzCBgmQ) by Nate B. Jones (February 2026).

See also: [The 5-Level Framework That Explains the AI Coding Gap](https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains) (companion article with exercises and resources).

---

## The Central Paradox

90% of Claude Code's codebase was written by Claude Code. Codex is shipping features built entirely by Codex. And yet a rigorous 2025 METR randomized control trial found that experienced open-source developers using AI tools completed tasks **19% slower** than developers working without them. Worse, those developers *believed* AI had made them 24% faster. They were wrong about both direction and magnitude.

A handful of teams are running lights-out software factories. The rest of the industry is getting measurably slower while convinced they're speeding up. The distance between these two realities is the most important gap in tech right now.

## The Five Levels of Vibe Coding

Dan Shapiro's framework maps where the industry actually stands:

- **Level 0 -- Spicy Autocomplete.** You type code, AI suggests the next line, you accept or reject. A faster tab key.
- **Level 1 -- Coding Intern.** You hand the AI a discrete, well-scoped task: write this function, build this component, refactor this module. You review everything.
- **Level 2 -- Junior Developer.** AI handles multi-file changes, navigates codebases, understands dependencies. You still read all the code. Shapiro estimates 90% of developers who consider themselves "AI-native" are here. They think they're farther along than they are.
- **Level 3 -- Developer as Manager.** You direct the AI and review at the feature/PR level. The model does implementation and submits PRs. Almost everybody tops out here because of the psychological difficulty of letting go of the code.
- **Level 4 -- Developer as Product Manager.** You write a specification, leave, come back hours later and check whether the tests pass. Code is a black box. This requires deep trust in the system and the ability to write specs that are complete enough to stand alone. Almost nobody has developed that skill yet.
- **Level 5 -- The Dark Factory.** A black box that turns specs into software. No human writes code. No human reviews code. The factory runs autonomously with the lights off.

## What Level Five Actually Looks Like

StrongDM's software factory is the most documented Level 5 system in production. Three engineers: Justin McCarthy, Jay Taylor, and Navan Chauhan. Running since July 2024, with the inflection point at Claude 3.5 Sonnet (fall 2024) -- when long-horizon agentic coding started compounding correctness more than compounding errors.

The factory runs on Attractor, an open-source coding agent. The repo is just three markdown specification files. The agent reads specs, writes code, and tests it.

### Scenarios vs. Tests

StrongDM doesn't use traditional software tests. They use **scenarios** -- and the distinction matters:

- **Tests** live inside the codebase. The AI can read them, which means it can optimize for *passing tests* rather than *building correct software*. Teaching to the test.
- **Scenarios** live outside the codebase. They're behavioral specifications describing what the software should do from an external perspective. The agent never sees the evaluation criteria during development. They function as a holdout set, the same concept ML uses to prevent overfitting.

When humans write code, gaming your own test suite isn't a typical failure mode. When AI writes code, optimizing for test passage is the *default behavior* unless you deliberately architect around it.

### Digital Twin Universe

Behavioral clones of every external service the software interacts with -- simulated Okta, Jira, Slack, Google Docs, Drive, Sheets. Agents develop against the twins, running full integration scenarios without touching production systems, real APIs, or real data.

Output to date: CXDB (their AI context store) -- 16,000 lines of Rust, 9,500 lines of Go, 700 lines of TypeScript. Shipped, in production.

Their benchmark for investment: $1,000 per engineer per day in tokens. Often still cheaper than the humans it replaces.

## The J-Curve of AI Adoption

The METR study result isn't surprising once you see the pattern. Developers spent time evaluating suggestions, correcting almost-right code, context-switching between their own mental model and the AI's output, and debugging subtle errors in generated code that *looked* correct but wasn't. 46% of developers in broader surveys say they don't trust AI-generated code.

This is the **J-curve**: when you bolt an AI coding assistant onto an existing workflow, productivity dips before it rises. The dip happens because the tool changes the workflow but the workflow hasn't been redesigned around the tool. New engine, old transmission; the gears grind.

Most organizations are sitting in the bottom of the J-curve right now. Many interpret the dip as evidence that AI doesn't work. GitHub Copilot: 20 million users, 55% faster on isolated lab tasks, but in production -- larger PRs, higher review costs, more security vulnerabilities. As one engineer put it: Copilot makes writing code cheaper but owning it more expensive.

The organizations seeing real gains (25-30%+) are the ones that redesigned their entire development workflow: how they write specs, how they review code, what they expect from junior vs. senior engineers, and how their CI/CD pipelines catch the new error categories that AI-generated code introduces. End-to-end process transformation. Not tool adoption.

## Organizational Structures Built for Humans

Every process in a software organization exists because humans building software in teams need coordination. Standups exist because developers working on the same codebase need to synchronize. Sprint planning exists because humans can only hold a certain number of tasks in working memory. Code review exists because humans make mistakes other humans catch. QA exists because builders can't evaluate their own work objectively.

Every one of these structures is a response to a human limitation. When the human is no longer writing the code, those structures aren't optional -- they're friction.

StrongDM's three-person team has no sprints, no standups, no Jira board. They write specs and evaluate outcomes. The entire coordination layer that constitutes the operating system of a modern software organization -- the layer that most managers spend 60% of their time maintaining -- is deleted. Not as a cost-saving measure, but because it no longer serves a purpose.

The engineering manager's value shifts from *coordinate the team building the feature* to *define the specification clearly enough that agents build the feature*. The program manager's value shifts from *track dependencies between human teams* to *architect the pipeline of specs that flow through the factory*. The center of gravity moves from **coordination** to **articulation**.

## The Brownfield Problem

Everything above assumes building from scratch. Most of the software economy is brownfield -- existing systems accumulated over years, running in production, carrying real revenue. CRUD apps with 15 years of organic feature growth. CI/CD pipelines tuned to one team's quirks. Config management that exists in the heads of three people who remember why that environment variable is set to that value.

You cannot dark-factory your way through a legacy system. The specification doesn't exist. Tests (if any) cover 30% of the codebase. The other 70% runs on institutional knowledge and tribal lore.

The system *is* the specification -- the only complete description of what the software does, because no one ever wrote down the thousand implicit decisions accumulated over a decade of patches, hotfixes, and "temporary" workarounds that became permanent.

The migration path:

1. **Use AI at Level 2-3** to accelerate existing work. Expect the J-curve dip.
2. **Use AI to document what your system really does** -- generating specs from code, building scenario suites that capture real behavior, creating holdout sets.
3. **Redesign CI/CD** for AI-generated code at volume -- different testing strategies, review processes, deployment gates.
4. **Shift new development to Level 4-5** while maintaining legacy in parallel.

Anyone telling you this is fast is selling something.

## The Spec Quality Bottleneck

The bottleneck has moved from implementation speed to specification quality. And spec quality is a function of how deeply you understand the system, the customer, and the problem. That understanding has always been the scarcest resource in software engineering. The dark factory doesn't reduce the demand for it -- it makes the demand absolute. It becomes the only thing that matters.

If you think writing a spec detailed enough for an AI agent to implement correctly without human intervention is trivial, you haven't tried it. Humans on the other end of a spec could fill gaps with judgment, context, a Slack message asking "did you mean X or Y?" The machines build what you described. If what you described was ambiguous, you get software that fills gaps with *software guesses*, not customer-centric guesses.

## The Junior Developer Pipeline

Junior developer employment is dropping 9-10% within six quarters of widespread AI tool adoption (2025 Harvard study). UK graduate tech roles fell 46% in 2024 with a further 53% drop projected by 2026. US junior developer postings have declined 67%.

The career ladder is getting hollowed out from underneath. The apprenticeship model -- juniors learn by writing simple features and fixing small bugs, seniors mentor and review -- breaks when AI handles the work juniors learned on. Seniors at the top, AI at the bottom, a thinning middle where learning used to happen.

And yet we need more excellent engineers than ever. The bar is rising toward systems thinking, customer intuition, and the ability to write specifications that anticipate questions the agent doesn't know to ask. Those skills always separated great engineers from adequate ones. The difference now is that adequate is no longer a viable career position, because adequate is what the models do.

Some organizations are moving toward a medical residency model: simulated environments where early-career developers learn by working alongside AI, reviewing AI output, developing judgment about what's correct and what's subtly wrong. Not the same as learning by writing code from scratch. But possibly better training for a world where the job is directing and evaluating AI output.

## Demand Never Saturates

Every time the cost of computing has dropped -- mainframes to PCs, PCs to cloud, cloud to serverless -- the total amount of software the world produced exploded. New categories that were economically impossible at the old cost structure became viable, then ubiquitous, then essential.

Every company in every industry needs software. Most of them -- a regional hospital, a mid-market manufacturer, a family logistics company -- can't afford to build what they need at current labor costs. A custom inventory system: half a million dollars, over a year. A patient portal integration: a third of a million.

Software production costs are dropping by an order of magnitude. That unmet need becomes addressable. The total addressable market is exploding. The constraint moves from *can we build it* to *should we build it* -- and *should we build it* has always been the harder question.

The dark factory doesn't replace the people who can answer that question. It amplifies them. A great product thinker with five engineers becomes a great product thinker with unlimited engineering capacity.

The machines have stripped away the camouflage of implementation complexity, and we're all about to find out how good we actually are at building software.
