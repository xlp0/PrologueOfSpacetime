# Backup and Recovery: Reversing Time

**Backup** represents **Time as a Reversible Function**. In mathematics, we say a function is reversible if we can recover the input from the output. Backups make time reversible—they allow us to undo the present and return to the past.

## The Principle

Memory preservation is the foundation of reliability. Like human memory, systems must preserve their past. Daily backups capture snapshots of system state, creating a timeline that enables time travel—the ability to restore to any previous moment.

### GASing Perspective: Gampang (Easy/Consistent)

*   **Concept**: Consistency through Redundancy
*   **Why it's Easy**: Complexity arises from change. By capturing snapshots at regular intervals, we transform continuous change into discrete, manageable states.
*   **Motto**: "The past is immutable; the future is recoverable."

## The Two-Layer Architecture

The PKC backup system operates through two independent processes working in harmony:

**The Daily Chronicler**  
Each day, a process awakens and captures the current state of the authentication system. It preserves:
*   User identities and their relationships
*   Authentication rules and policies
*   The configuration of the system itself

This snapshot is compressed and sent to object storage, creating a point in time we can return to if needed.

**The Continuous Guardian**  
Periodically, a second process scans the local archive and compares it to the remote storage. If any backup has vanished—whether through accident or malice—it is automatically restored. This creates a **self-healing memory system** where human errors cannot cause permanent amnesia.

### Why Two Independent Systems?

This embodies the **coproduct type** from type theory: protection can come via the daily backup OR via the continuous sync. Both paths lead to data preservation, creating redundancy that survives single points of failure.

This is not mere duplication—it is **defense in depth**. The first layer creates backups; the second layer protects those backups from deletion. Together, they form a system more resilient than either alone.

## Recovery: Reversing Time

When disaster strikes, recovery procedures transform the abstract concept of "backup" into concrete action. The process follows a clear path:

1. **Identify the point of return** - Which backup represents the desired past state?
2. **Retrieve the memory** - Download the backup from MinIO storage
3. **Restore the state** - Apply the backup to recreate the past
4. **Verify the restoration** - Confirm the system matches the expected state

Recovery time is measured in minutes—the time required to travel backward through the system's timeline and restore a previous state.

## Verification

How do we know the backups work?

The system maintains a manifest—a record of what should exist. Each backup is verified:
*   **Integrity checks** ensure files aren't corrupted
*   **Automated restoration tests** prove backups can actually be used
*   **Audit trails** track every backup creation and restoration

**Current State**: Multiple backups spanning several weeks, all verified and accessible.

## The 3-2-1 Rule

The PKC backup strategy follows an ancient principle: **3** copies of data, on **2** different storage types, with **1** copy off-site. This rule has protected organizations for decades because it ensures no single failure can destroy all copies.

## Data Replication: Spatial Redundancy

**Data Replication** represents **Spatial Redundancy**. While backups provide temporal redundancy (copies across time), replication provides spatial redundancy (copies across space). Together, they form a complete protection strategy.

### The Synchronizer

Object storage currently operates on a single machine with plans to expand to multiple locations. This expansion will create an **active-active mesh**—a network where all nodes are equals, each capable of serving requests and each maintaining identical data.

**Active-Active vs. Active-Passive**

Traditional replication uses an active-passive model: one primary copy serves requests while passive copies wait in standby. Active-active replication is fundamentally different—all copies are primary. Users can write to any location, and changes propagate to all others.

This is analogous to the **product type** in type theory: to prove a proposition, you need evidence at location A AND location B AND location C. All locations must agree.

### The Replication Flow

When a backup file is saved to object storage:
1. The write is acknowledged immediately (fast user experience)
2. In the background, the file is copied to other locations
3. Within moments, all locations hold identical copies

If one location fails, users automatically connect to another. The failure is invisible—no restoration needed, no downtime experienced.

## Disaster Recovery Scenarios

The PKC infrastructure plans for failures at multiple scales:

**Service-Level Failures**  
A single replica crashes. Recovery: Automatic within minutes. User impact: None.

**Node-Level Failures**  
An entire machine becomes unavailable. Recovery: Automatic within minutes. User impact: Slight performance degradation during recovery.

**Data-Level Failures**  
Database corruption or accidental deletion. Recovery: Manual restoration from backup. User impact: Brief service interruption.

**Site-Level Failures**  
Complete infrastructure loss. Recovery: Manual rebuild from backups and documentation. User impact: Extended outage.

## The Practice of Testing

Untested recovery procedures are theoretical, not practical. The PKC infrastructure practices recovery through:

**Monthly Backup Tests**  
Restore a backup to a test environment and verify functionality. This proves backups actually work and trains operators in recovery procedures.

**Quarterly Disaster Recovery Drills**  
Simulate complete service failure and execute full recovery. This identifies gaps in documentation and builds team confidence.

**Continuous Monitoring**  
Automated health checks detect failures within seconds, enabling rapid response before users notice problems.
