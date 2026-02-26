# Palgebra Graph Visualization: The UX of Computational Structure

*Extracted from the 2026-02-26 field notes.*

## Kanban vs. Palgebra Graphs
Standard project management dashboards and Kanban boards show *task state*: what is blocked, what is in progress, who owns what. They capture the state of work items.

A Palgebra Graph visualization must show *computational structure*: which transformations are composing with which, where the fan output feeds into the funnel, and which specific nodes act as bottlenecks in the epistemic flow. 

For example: A task can show as "in progress" on a Kanban board while internally waiting on three upstream text transformations to resolve. The Kanban board is legible to anyone; the Palgebra Graph is for understanding the underlying compositional architecture.

## The Blackbody Heat Encoding Proposal
Visualizing an active multi-agent pipeline requires indicating where attention and compute are currently focused. 

The proposed encoding utilizes **blackbody radiation heat mapping**:
- **White-Hot:** This node/transformation is the current center of intense deliberative activity.
- **Red/Dark Red:** The deliberative activity is cooling or has recently finished.
- **Cool/Dark:** Idle or settled nodes.

### Why this works
This encoding carries both intensity and temporal data intuitively without requiring a complex legend. The color space itself is the information.

This pattern is deeply precedented in distributed systems engineering (e.g., Jaeger traces, service mesh dashboards) where latency and error rates appear as colors on a dependency graph. The Palgebra Graph UI simply applies this distributed systems pattern to narrative computation networks.

## Next Steps for Taming
- Mock up a visual representation of a standard `/committee` run using the blackbody radiation palette.
- Define a lightweight schema that the Cyberneutics Director can emit to power this UI dynamically.
