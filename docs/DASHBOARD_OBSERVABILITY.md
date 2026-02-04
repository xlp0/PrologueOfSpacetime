# Observability: Seeing Systems as Living Spaces

## Introduction

Observability transforms how we understand running systems. Rather than treating infrastructure as opaque machinery, observability reveals the **living patterns** within—the flows of data, the rhythms of user interaction, the health of interconnected components. This document explores how the PKC Landing Page project implements observability as a practice of **continuous awareness**, where systems become visible, understandable, and responsive.

In the same way that Homotopy Type Theory treats types as **spaces** inhabited by **points**, observability treats systems as **contexts** inhabited by **events**. Each metric is a point in time, each log entry a trace of execution, each dashboard a window into the topology of system behavior.

---

## Understanding Observability

### What Observability Reveals

Observability is the practice of making internal system states visible through external outputs. The PKC infrastructure observes:

*   **System Health:** The vitality of cluster nodes, the availability of services, the responsiveness of applications
*   **User Behavior:** How people navigate the application, which components they visit, where they encounter friction
*   **Authentication Patterns:** Login flows, session lifecycles, security events
*   **Resource Dynamics:** The ebb and flow of CPU usage, memory consumption, network traffic

### The Three Pillars

Traditional observability rests on three foundations:

1. **Metrics** - Numerical measurements over time (CPU usage, request counts, response times)
2. **Logs** - Textual records of discrete events (errors, state changes, user actions)
3. **Traces** - The paths that requests take through distributed systems

The PKC implementation extends this with a fourth pillar:

4. **User Experience** - Real user monitoring that captures how the system feels to those who use it

### Observability as Context Transformation

In the framework of the Prologue of Spacetime, observability functions as a **type family** that maps system states to visualization contexts. Each dashboard is a **dependent function** where the displayed information depends on the current state of the infrastructure. When a node fails, the dashboard context transforms—new alerts appear, metrics shift, the visual representation adapts to reflect the changed reality.

---

## The Observability Architecture

### A System of Nested Contexts

The PKC observability infrastructure resembles the **nested universes** of Homotopy Type Theory. Each layer contains and contextualizes the layer below, creating a hierarchy of awareness:

**The User Layer**  
At the outermost layer, users interact with the PKC Landing Page through their browsers. Their actions—clicks, navigation, component visits—generate events that flow into the observability system. This is where experience becomes data.

**The Collection Layer**  
Beneath the user experience, collection mechanisms gather signals from multiple sources:
*   **Faro SDK** captures user interactions and frontend performance
*   **Prometheus** periodically samples system metrics from cluster nodes
*   **Promtail** streams log entries from running applications

**The Storage Layer**  
Collected data flows into specialized storage systems:
*   **Prometheus** holds recent time-series metrics (15 days)
*   **Loki** aggregates logs with efficient indexing
*   **Thanos** extends metric retention for historical analysis

**The Visualization Layer**  
Grafana queries these storage systems and renders dashboards—visual representations that transform raw data into comprehensible patterns. Each dashboard is a **projection** that extracts meaning from the underlying data space.

**The Archive Layer**  
Daily, automated processes export metrics to MinIO object storage, creating a permanent historical record. This enables trend analysis across months and years, revealing patterns invisible in shorter timeframes.

### Data as Paths Through Space

In observability, we can think of data flow as **path composition**:

1. A user action creates an event (a point in the user experience space)
2. The Faro SDK maps this event to a log entry (a path to the collection space)
3. Prometheus scrapes this as a metric (a path to the storage space)
4. Grafana queries and visualizes it (a path to the representation space)
5. GitHub Actions archives it (a path to the historical space)

Each transformation preserves essential information while changing context—much like how **functors** in category theory map between spaces while respecting their structure.

---

## Windows into System Behavior

### The Dashboard as Lens

The PKC infrastructure maintains over 30 dashboards, each offering a different perspective on system health. Rather than listing technical specifications, we can understand these dashboards as **lenses** that focus attention on specific aspects of system behavior.

### Categories of Observation

**Infrastructure Awareness (15 dashboards)**  
These dashboards reveal the health of the underlying platform—the Kubernetes cluster that orchestrates all services. They answer questions like:
*   Is the control plane responding quickly to requests?
*   Are cluster resources distributed efficiently across nodes?
*   Which applications consume the most compute power?
*   How does network traffic flow between services?

**Node Vitality (5 dashboards)**  
Individual machines form the foundation of the cluster. These dashboards monitor:
*   The health status of each physical or virtual machine
*   Resource utilization patterns across different nodes
*   Network connectivity, especially for remote nodes accessed via ZeroTier VPN
*   System-level metrics like disk usage, CPU load, and memory pressure

**Authentication Flows (1 dashboard)**  
A specialized dashboard tracks user authentication through ZITADEL:
*   How many users are actively logged in
*   Patterns in login attempts (successful and failed)
*   Token generation and session lifecycle events
*   Security-relevant events that might indicate issues

**System Components (9+ dashboards)**  
These observe the health of the observability system itself and supporting services:
*   Prometheus metric collection performance
*   Grafana dashboard rendering speed
*   Log aggregation system status
*   DNS resolution performance
*   Alert routing and notification delivery

### Notable Dashboard Examples

**The Node Health Dashboard**  
This dashboard provides a unified view of all cluster machines, including remote nodes connected via ZeroTier VPN. It reveals:
*   Which nodes are healthy and accepting workloads
*   Resource consumption patterns across the infrastructure
*   Network connectivity status for geographically distributed nodes
*   Early warning signs of capacity constraints

The dashboard monitors seven nodes: a control plane machine, five worker nodes, and a network-attached storage system. Each appears with its hostname rather than IP address, making the visualization immediately comprehensible.

**The ZITADEL Authentication Dashboard**  
Authentication is the gateway to the system. This dashboard tracks:
*   Active user sessions and registration trends
*   Login success and failure patterns
*   Token generation and session lifecycle events
*   OAuth2 flows and external authentication providers

By monitoring authentication events, the system can detect both normal usage patterns and potential security concerns—failed login spikes, unusual token requests, or session anomalies.

**The Prometheus Overview**  
Since Prometheus collects metrics from all other components, monitoring Prometheus itself is essential. This meta-dashboard reveals:
*   How efficiently Prometheus scrapes metrics from targets
*   The volume of time-series data being stored
*   Query performance and resource utilization
*   Storage consumption trends

When Prometheus struggles, all other dashboards suffer. This dashboard serves as an early warning system for the observability infrastructure itself.

---

## The Rhythm of Collection

### Automated Awareness

Observability requires continuous attention, but human attention is finite. The PKC infrastructure automates the collection of metrics.

This automation embodies a principle from the Prologue of Spacetime: **systems should observe themselves**. Just as consciousness arises from the brain observing its own states, system awareness emerges from automated self-monitoring.

### The Collection Process

Each morning, an automated workflow:

1. **Gathers** metrics from all active dashboards
2. **Transforms** raw data into structured formats
3. **Generates** human-readable reports with visualizations
4. **Archives** everything to long-term storage
5. **Preserves** a 30-day backup in the repository

This daily rhythm creates a historical record—a memory that extends beyond the 15-day retention of the real-time monitoring system. Patterns invisible in short timeframes become visible across weeks and months.

### The Archive as Memory

Collected metrics flow into MinIO object storage, organized by date. Each day creates a new folder containing:

*   JSON files with structured metric data
*   Markdown reports with visualizations
*   Summary files tracking collection success
*   Authentication analytics with trend analysis

This archive serves multiple purposes:
*   **Historical Analysis** - Comparing current behavior to past patterns
*   **Capacity Planning** - Projecting future resource needs from growth trends
*   **Incident Investigation** - Reconstructing system state during past events
*   **Compliance** - Maintaining audit trails for security and operations

The archive is publicly accessible, embodying the PKC principle of **transparent operations**. Anyone can examine the system's historical behavior.

---

## Sources of Truth

### The Data Landscape

Observability data flows from multiple sources, each specialized for different types of information. Understanding these sources reveals how the system constructs its self-awareness.

### Prometheus: The Metric Collector

Prometheus serves as the primary metric storage system, sampling numerical measurements every 15-30 seconds. It maintains a 15-day rolling window of data—recent enough for operational decisions, old enough to reveal short-term trends.

Prometheus embodies the **universal quantifier** from type theory: for every monitored target, it provides a metric collection function. No node, pod, or service escapes its periodic sampling. This completeness ensures comprehensive visibility.

**Bridging Physical Distance**  
The PKC cluster spans multiple locations. Some nodes sit in the same data center, while others connect from remote sites. To monitor these distributed nodes, the system uses ZeroTier VPN—an overlay network that makes geographically separated machines appear as neighbors.

Prometheus cannot directly reach remote nodes, so nginx proxy pods act as bridges. Each proxy forwards metrics from a remote node's ZeroTier address to Prometheus. This architecture demonstrates the **coproduct type** from type theory: metrics can arrive via direct connection OR via proxy, and both paths are equally valid.

### Thanos: Extended Memory

While Prometheus retains 15 days of metrics, Thanos extends this memory indefinitely. It aggregates data from multiple Prometheus instances and stores it in long-term object storage, then provides a unified query interface.

Thanos enables **temporal analysis**—comparing this week's behavior to last month's, or tracking resource growth over quarters. It transforms observability from a real-time practice into a historical discipline.

### Loki: The Log Aggregator

Logs tell stories that metrics cannot. While metrics reveal "CPU usage is 80%," logs explain "the authentication service restarted due to memory pressure." Loki collects these textual narratives from all applications and makes them searchable.

The PKC Loki deployment currently experiences partial degradation—some components struggle while others function. This imperfection itself teaches an observability lesson: systems exist in states between perfect health and complete failure. Observability must accommodate partial functionality.

### Alertmanager: Attention Direction

Not all observations require immediate human attention. Alertmanager filters the continuous stream of metrics, identifying conditions that warrant notification. It groups related alerts, suppresses duplicates, and routes notifications to appropriate channels.

This embodies the **negation** concept from type theory: an alert is a function that maps normal system states to the empty type (no action needed) and problematic states to notification types (action required).

### Faro: User Experience Observation

While Prometheus and Loki observe infrastructure, Faro observes users. Embedded in the frontend application, it captures:
*   Which components users visit and how long they stay
*   Navigation patterns through the application
*   JavaScript errors that disrupt user experience
*   Performance metrics like page load times

Faro transforms user experience from subjective impression into measurable data. It answers questions like "Do users actually engage with this feature?" and "Where do they encounter friction?"

---

## Observing Across Distance

### The Challenge of Distribution

Modern infrastructure rarely exists in a single location. The PKC cluster includes machines in different physical spaces—some in the same data center, others connected remotely. Traditional monitoring assumes all nodes share a network, but reality is messier.

### ZeroTier: Creating Virtual Proximity

ZeroTier VPN creates an overlay network that makes distant machines appear as neighbors. Seven nodes—a control plane, five workers, and a storage system—connect through this virtual space. Each receives a consistent address in the overlay network, regardless of its physical location.

This architecture embodies a key observability principle: **abstraction enables observation**. By abstracting away physical network topology, ZeroTier makes all nodes equally observable.

### The Proxy Pattern

Prometheus cannot directly reach nodes on the ZeroTier network, so the system employs proxy pods as intermediaries. Each proxy:
*   Runs on a node with access to both networks
*   Forwards metric requests from Prometheus to remote nodes
*   Returns responses back through the same path

Five proxies handle five remote nodes, each listening on a dedicated port. This pattern demonstrates **separation of concerns**: Prometheus focuses on metric collection, proxies handle network translation.

### Human-Readable Labels

Technical systems often display IP addresses—opaque identifiers meaningful to machines but not humans. The PKC monitoring system transforms these addresses into hostnames through label relabeling. Instead of seeing "10.40.14.68", dashboards show "itdelb200b".

This seemingly small change profoundly impacts usability. When investigating an issue, operators immediately recognize "hpserver is struggling" rather than having to mentally map "10.40.14.205 has high CPU".

### The Current State

Six of seven nodes report healthy status. The seventh—a network storage system—shows connectivity issues. This partial failure state is typical of real infrastructure. Observability must reveal not just binary health/failure states, but the nuanced reality of systems operating at various levels of functionality.

---

## Automated Reporting

### From Data to Narrative

Raw metrics tell incomplete stories. Numbers like "1,247 authentication events" lack context. The PKC system transforms metrics into narrative reports that explain what the numbers mean.

### The ZITADEL Authentication Report

Each day, the system generates a comprehensive report analyzing authentication patterns. This report includes:

*   **User Growth Trends** - How the user base evolves over time
*   **Authentication Patterns** - When users log in, which methods they use
*   **Event Distribution** - The types of authentication events occurring
*   **Visual Representations** - Charts that make patterns immediately visible

These reports use Mermaid.js for visualization, creating diagrams that render directly in Markdown. This choice reflects the PKC philosophy: documentation should be readable as plain text yet rich when rendered.

### The Value of Synthesis

Individual metrics answer specific questions: "How many users logged in today?" But synthesized reports answer broader questions: "Is user engagement growing?" "Are authentication failures increasing?" "Which login methods do users prefer?"

This synthesis transforms observability from reactive monitoring (responding to alerts) into proactive understanding (recognizing trends before they become problems).

---

## Querying the Observable Universe

### The Language of Questions

Observability systems provide query languages—specialized syntaxes for asking questions about system behavior. These languages transform vague curiosities ("Is the system healthy?") into precise queries that return measurable answers.

### Two Query Paradigms

**LogQL: Searching Narratives**  
Loki's query language treats logs as text to be searched and filtered. Questions like "Show me all authentication errors in the last hour" or "Which components are users visiting most?" become queries that scan log streams for matching patterns.

LogQL embodies the **existential quantifier**: "Does there exist a log entry matching these criteria?" The query returns all inhabitants of the log space that satisfy the specified properties.

**PromQL: Analyzing Time Series**  
Prometheus's query language treats metrics as mathematical functions over time. Questions like "What's the average CPU usage across all nodes?" or "How many pods restarted in the last day?" become calculations performed on time-series data.

PromQL enables **aggregation and transformation**—taking raw measurements and deriving insights. A simple metric like "CPU seconds" becomes "CPU utilization percentage" through mathematical transformation.

### From Queries to Understanding

Query languages are tools, not ends in themselves. The goal is not to master syntax but to develop **query intuition**—the ability to translate operational questions into data queries. This intuition grows through practice and pattern recognition.

The PKC system provides example queries for common questions, but the real skill lies in formulating new questions as situations arise. Observability becomes powerful when operators can ask questions the system designers never anticipated.

---

## Integrating Observability

### Making Systems Observable

Observability is not a feature added at the end—it must be woven into system design from the beginning. The PKC Landing Page demonstrates this through monitoring integrated at multiple layers.

### User Experience Tracking

The frontend application embeds Faro SDK to capture user interactions transparently. Each component visit, navigation event, and performance metric flows automatically into the observability system without requiring explicit tracking code everywhere.

### Dashboard Embedding

Grafana dashboards can be embedded directly into applications using iframes, making system health visible to end users. The PKC Landing Page includes embedded dashboards that update in real-time, demonstrating the principle of **transparent operations**.

### Component Metadata

Each component in the CLM registry includes observability metadata—expected performance characteristics, associated dashboards, health check endpoints. This creates a bidirectional link between application structure and observability infrastructure.

---

## When Systems Struggle

### Understanding Degradation

Perfect systems exist only in theory. Real infrastructure operates in various states of partial functionality. The PKC observability system itself demonstrates this—some Loki components struggle while others function normally.

### Common Patterns of Failure

**Log Aggregation Issues**  
The Loki distributed system shows partial degradation. The distributor accepts logs, but the ingester and querier components restart frequently. This affects historical log queries while real-time logging continues.

This pattern teaches an important lesson: **distributed systems fail partially**. Observability must reveal not just binary health states but the nuanced reality of systems operating at reduced capacity.

**Missing Metrics**  
When dashboards show "No data," the issue might lie anywhere in the collection chain—the monitored service, the metric exporter, the network path, Prometheus scraping, or the dashboard query itself. Troubleshooting requires understanding this entire path.

**Proxy Connectivity**  
Remote nodes monitored via ZeroTier VPN depend on proxy pods. When a proxy fails, that node becomes invisible to monitoring. The system must detect not just application failures but failures in the observability infrastructure itself.

### The Practice of Diagnosis

Effective troubleshooting follows a pattern:

1. **Observe the symptom** - What specific behavior indicates a problem?
2. **Hypothesize the cause** - What could produce this symptom?
3. **Test the hypothesis** - Query logs, check metrics, inspect configurations
4. **Iterate** - If the hypothesis proves wrong, form a new one

This mirrors the scientific method. Observability provides the instruments for measurement; human judgment interprets the results.

---

## Principles of Effective Observability

### Design for Visibility

Systems should be **observable by default**. Rather than adding monitoring as an afterthought, design components to expose their internal state naturally. Metrics endpoints, structured logging, and health checks should be fundamental, not optional.

### Balance Detail and Clarity

Too little information leaves operators blind. Too much creates noise that obscures important signals. Effective observability finds the balance—capturing enough detail to diagnose issues while presenting information clearly enough to recognize patterns.

### Embrace Imperfection

No monitoring system captures everything. Metrics have gaps, logs get lost, dashboards sometimes mislead. Observability practitioners develop **informed skepticism**—trusting the data while recognizing its limitations.

### Automate Routine Observation

Human attention is precious and finite. Automate the routine—daily metric collection, standard reports, threshold alerts—so humans can focus on investigation, pattern recognition, and system improvement.

### Document for Future Selves

Today's obvious solution becomes tomorrow's mystery. Document not just what the system does but why—the reasoning behind dashboard designs, the meaning of specific metrics, the history of configuration choices. Future operators (including your future self) will thank you.

---

## Prologue of Spacetime Integration

### Observability as Type Theory

The PKC observability infrastructure demonstrates principles from Homotopy Type Theory in practice:

**Types as Spaces**  
Each dashboard represents a **space** of possible system states. Metrics are **points** within these spaces. A CPU usage metric at 80% is a specific point in the resource utilization space.

**Paths as State Transitions**  
When CPU usage moves from 40% to 80%, this represents a **path** through the state space. Multiple paths can connect the same states—CPU might increase gradually or spike suddenly. These different paths have different meanings for system health.

**Dependent Functions**  
Alerting rules are **dependent functions** where the output type (alert or silence) depends on the input value (the metric). When CPU exceeds 90%, the function maps to the alert type. Below that threshold, it maps to the empty type (no alert).

**Universal Quantifiers**  
Prometheus embodies the **universal quantifier**: for every monitored target, it provides a metric collection function. This completeness ensures comprehensive visibility—no component escapes observation.

**Propositions as Types**  
An alert is a **proposition** that the system is in an unhealthy state. The alert's existence (inhabitant of the alert type) serves as **proof** of the problem. Multiple alerts for the same issue represent multiple proofs of the same proposition.

### The Living System

Observability reveals systems as **living entities** rather than static machinery. They breathe (resource usage oscillates), they remember (metrics accumulate history), they communicate (logs tell stories), they adapt (autoscaling responds to load).

The PKC infrastructure has operated for over 50 days—a lifetime measured in continuous observation. During this time, it has collected millions of metrics, aggregated countless logs, generated daily reports, and maintained awareness of its own state.

This continuous self-observation creates a form of **system consciousness**—not sentience, but awareness. The system knows its own performance, recognizes its own failures, and records its own history.

---

## Conclusion

Observability is not merely monitoring—it is the practice of making systems comprehensible. The PKC Landing Page demonstrates this through an infrastructure that observes itself at multiple scales: individual metrics, aggregated dashboards, automated reports, and historical archives.

The system embodies key principles:
*   **Transparency** - Operations are visible to all
*   **Automation** - Routine observation happens without human intervention
*   **Resilience** - Partial failures are detected and accommodated
*   **Evolution** - The system learns from its own history

As the Prologue of Spacetime explores how meaning emerges from structure, observability reveals how understanding emerges from data. Raw metrics become information, information becomes insight, and insight enables improvement.

The infrastructure described here will continue evolving. New dashboards will emerge, metrics will be refined, collection processes will improve. But the fundamental practice remains: **making the invisible visible**, transforming opaque systems into comprehensible spaces that humans can understand and improve.