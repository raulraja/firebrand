---
predictable: spec
---
## Specification Details
- **ID:** SPEC-008
- **Name:** org/firebrandocm/dao/cql/clauses/ClauseComparator.java

### Description
`ClauseComparator.java` — Clause comparator. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. `ClauseComparator` carries `statement`. Checks: “`ClauseComparator.compare` only works when `clauseOrder` is not null.” 1 requirement: 1 verified.

### Types

`ClauseComparator` — Declares 1 operation:
- `compare`(`clause`, `otherClause`) — requires `clauseOrder` is not null [verified]

A `[verified]` requirement is one the operation checks itself.

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Analysis

#### ClauseComparator.compare <!-- predictable:group -->

##### ANL-0016 [implemented, verified]
`ClauseComparator.compare` only works when `clauseOrder` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=ClauseComparator.compare -->

<!-- predictable:vc=il1.null-dereference -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/clauses/ClauseComparator.java:45-49](../../../../../../src/main/java/org/firebrandocm/dao/cql/clauses/ClauseComparator.java#L45-L49)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-008/ANL-0016.md -->
