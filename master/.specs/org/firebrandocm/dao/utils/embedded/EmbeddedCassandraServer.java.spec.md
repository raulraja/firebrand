---
predictable: spec
---
## Specification Details
- **ID:** SPEC-006
- **Name:** org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java

### Description
`EmbeddedCassandraServer.java` — Embedded cassandra server. Called from `AbstractPersistenceFactory.destroy` and `AbstractPersistenceFactory.init`, and possibly from places the call graph cannot see. `EmbeddedCassandraServer` carries `logger`, `baseDirectory`, `cassandraDaemon`, `cassandraThread` and `cleanupDirectories`. Observed: “At line 95: A failure is caught and cannot be reported.” 3 requirements: 3 violated.

### Types

`EmbeddedCassandraServer` — Declares 6 operations:
- `getBaseDirectory`() — no requirement inferred
- `setCleanupDirectories`(`cleanupDirectories`) — no requirement inferred
- `start`() — “starts embedded Cassandra server.” — no requirement inferred
- `cleanupDirectoriesFailover`() — “Cleans up cassandra's temporary base directory.” — At line 95: A failure is caught and cannot be reported; at line 100: A failure is caught and cannot be reported; a request to stop is caught and ignored
- `cleanupDirectories`() — “Cleans up cassandra's temporary base directory.” — no requirement inferred
- `stop`() — “Stops embedded Cassandra server.” — no requirement inferred

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, violated]` — the analysis found a case where the condition fails.
`[violated]` on the card above and `[implemented, violated]` on a row below are one state.

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Behaviours

#### EmbeddedCassandraServer.cleanupDirectoriesFailover <!-- predictable:group -->

##### BEH-0002 [implemented, violated]
At line 95: A failure is caught and cannot be reported. The failure is caught and nothing is returned, so callers get the same value whether the work failed or succeeded. The work is silently lost. Safe to rely on when this function reports the failure to its caller, by an answer or by letting it out.

<!-- predictable:behaviour -->

<!-- predictable:subject=EmbeddedCassandraServer.cleanupDirectoriesFailover -->

<!-- predictable:vc=site.failure-swallowed-without-saying-so.-.9b530df0-0 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java:95](../../../../../../src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java#L95)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-006/BEH-0002.md -->

##### BEH-0003 [implemented, violated]
At line 100: A failure is caught and cannot be reported. The failure is caught and nothing is returned, so callers get the same value whether the work failed or succeeded. The work is silently lost. Safe to rely on when this function reports the failure to its caller, by an answer or by letting it out.

<!-- predictable:behaviour -->

<!-- predictable:subject=EmbeddedCassandraServer.cleanupDirectoriesFailover -->

<!-- predictable:vc=site.failure-swallowed-without-saying-so.-.9b530df0-1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java:100](../../../../../../src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java#L100)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-006/BEH-0003.md -->

##### BEH-0004 [implemented, violated]
A request to stop is caught and ignored. The handler catches the cancellation signal and carries on, so cancelled work runs to the end. Whoever asked it to stop cannot tell that it did not. Safe to rely on when a cancellation that reaches this function is passed on to its caller.

<!-- predictable:behaviour -->

<!-- predictable:subject=EmbeddedCassandraServer.cleanupDirectoriesFailover -->

<!-- predictable:vc=site.cancellation-swallowed.-.3dc0dd85 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java:100](../../../../../../src/main/java/org/firebrandocm/dao/utils/embedded/EmbeddedCassandraServer.java#L100)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-006/BEH-0004.md -->
