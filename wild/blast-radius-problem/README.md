# The Blast Radius Problem in Declarative Systems

*Extracted from the 2026-02-26 field notes.*

## The Context
Declarative systems (like NixOS fleet management or large-scale Kubernetes deployments) model configuration as code. This makes them highly suited to generic agent workflows because the semantics are clean and reproducible. A single "developer agent" can usually write plausible Nix configuration easily.

## The Problem
Fleet management possesses a sharp asymmetry that undifferentiated developer agents are not designed to handle: **The configuration space is large and text-based (easy for LLMs), but the failure modes are concrete, immediate, and potentially catastrophic.**

A bad configuration switch pushed across a fleet is not always easily rolled back—especially if the error breaks networking, SSH access, or boot configurations. 

### Why Developer Agents Fail Here
An undifferentiated developer agent focuses on construction. It will not intuitively stop to ask:
- What happens to running service X when this lands?
- What is the out-of-band rollback path?
- Is this safe to apply incrementally across the fleet, or does it require a coordinated cutover?

These questions represent qualitatively different cognitive postures. 

## The Solution: Role Differentiation as Load-Bearing Architecture
To safely operate in environments with asymmetric blast radiuses, the agent committee requires enforced, distinct roles:
1. **The Planner / Developer:** Optimizes for declarative construction. 
2. **The Tester (Adversarial):** Optimizes for finding edge cases, regressions, and structural weaknesses in the Planner's code.
3. **The Operator:** Evaluates the live fleet state, the deployment strategy, and the rollback viability. 

In this domain, role differentiation is not bureaucratic overhead—it is fundamental load-bearing architecture.

## Next Steps for Taming
- Design a formal committee roster specifically tuned for Dev/Ops configuration tasks.
- Create a test scenario demonstrating a developer agent succeeding at construction but failing at deployment safety, compared against a deliberative committee that catches the blast radius implications.
