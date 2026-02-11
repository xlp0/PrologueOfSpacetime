# High Availability: Existence Through Replication

**High Availability** represents **Existence through Replication**. In type theory, we say a type is inhabited if it contains at least one term. High availability ensures a service type remains inhabited even when individual terms (instances) disappear.

## The Principle

No single component is irreplaceable. Multiple copies of each service run simultaneously, distributed across physical machines. When one fails, others continue seamlessly. This is the **Universality** principle made operational: the **Terminal Object** (the service abstraction) provides a unique sink toward which all replicas point, ensuring that the system's identity is preserved regardless of which individual instance serves the request.

### GASing Perspective: Susah (Hard/Reliable)

*   **Concept**: Reliability through Complexity
*   **Why it's Hard**: Coordinating multiple copies is more complex than running a single instance. But this complexity buys reliability—the system survives failures that would destroy simpler architectures.
*   **Motto**: "One is fragile; three is resilient."

## The Replicator

The PKC infrastructure runs three copies of the ZITADEL authentication service, each on a different physical machine. This is not mere duplication—it is **strategic distribution**.

**Why Three?**

The number three provides optimal balance:
*   **Two** would provide redundancy, but no margin for error
*   **Three** allows one to fail while maintaining redundancy in the remaining two
*   **More than three** increases cost without proportional benefit

**The Distribution Strategy**

Each replica runs on a separate machine across the distributed infrastructure. The orchestration system ensures they never colocate—if a machine fails, only one replica is lost. The others continue serving users seamlessly.

## Verification

How do we know high availability works?

The system maintains **health probes**—periodic checks that verify each replica is functioning:
*   **Liveness probes** detect when a replica has crashed
*   **Readiness probes** determine when a replica can accept traffic

When a probe fails, Kubernetes automatically:
1. Removes the failed replica from the service pool
2. Schedules a replacement on a healthy machine
3. Waits for the new replica to pass health checks
4. Adds it back to the service pool

**Current State**: Multiple replicas running, distributed across separate machines, all healthy, serving traffic with balanced load distribution.

## The Cluster as Organism

The PKC infrastructure consists of multiple machines forming a distributed organism:

**The Control Plane**  
Multiple machines serve as the cluster's "brain"—they coordinate all activities, schedule workloads, and maintain the desired state. Having redundant control planes means the cluster can survive the loss of one brain and continue functioning.

**The Worker Nodes**  
Several machines execute the actual workloads. They are the "body" that performs the work coordinated by the brain.

**The Database Layer**

The authentication system's database also practices redundancy. Two PostgreSQL instances run simultaneously:
*   A **primary** instance handles all writes
*   A **replica** instance mirrors the primary's data

If the primary fails, the replica automatically promotes itself to primary within moments. Applications reconnect automatically—the failure is invisible to users.

## Load Distribution

When a user connects to the identity provider, they don't connect to a specific replica. Instead, they connect to a **service**—an abstraction that represents all healthy replicas.

The orchestration system distributes incoming requests across replicas using balanced algorithms. This ensures no single replica becomes overloaded.

## Graceful Degradation

Systems fail in stages, not all at once. The PKC infrastructure is designed to degrade gracefully:

**Single Replica Failure**  
Impact: Partial capacity reduction  
User Experience: Slightly slower responses, but service continues  
Recovery: Automatic within minutes

**Single Node Failure**  
Impact: Loss of all replicas on that node  
User Experience: Brief slowdown during rescheduling  
Recovery: Automatic within minutes

**Database Primary Failure**  
Impact: Brief write interruption  
User Experience: Login attempts may need retry  
Recovery: Automatic within seconds

This layered resilience means the system can survive multiple simultaneous failures before becoming unavailable.
