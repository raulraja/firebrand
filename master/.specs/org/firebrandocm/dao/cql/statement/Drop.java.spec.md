---
predictable: spec
---
## Specification Details
- **ID:** SPEC-010
- **Name:** org/firebrandocm/dao/cql/statement/Drop.java

### Description
`Drop.java` — Drop. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. `Drop` carries `TYPES` and `ORDER`. REFUTED: “`Drop.build` only works when 0 is at most 0 and 0 is less than the `length` of the `clauses` of the `Drop`.” 2 requirements: 1 violated, 1 verified.

### Types

`Drop` — Declares 2 operations:
- `build`() — requires 0 is at most 0 and 0 is less than the `length` of the `clauses` of the `Drop` [violated]; `type` is not null [verified]
- `getClausesOrder`() — no requirement inferred

A `[verified]` requirement is one the operation checks itself.

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, violated]` — the analysis found a case where the condition fails.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other one.

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Analysis

#### Drop.build <!-- predictable:group -->

##### ANL-0018 [implemented, violated]
`Drop.build` only works when 0 is at most 0 and 0 is less than the `length` of the `clauses` of the `Drop`.

<!-- predictable:analysis -->

<!-- predictable:subject=Drop.build -->

<!-- predictable:vc=il1.bounds -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/statement/Drop.java:112-119](../../../../../../src/main/java/org/firebrandocm/dao/cql/statement/Drop.java#L112-L119)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-010/ANL-0018.md -->

##### ANL-0019 [implemented, verified]
`build` throws `IllegalArgumentException` unless `type` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=Drop.build -->

<!-- predictable:vc=il2.domain-guard -->

<!-- predictable:throws=IllegalArgumentException -->

<!-- predictable:canonical=`Drop.build` only works when `type` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/statement/Drop.java:112-119](../../../../../../src/main/java/org/firebrandocm/dao/cql/statement/Drop.java#L112-L119)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-010/ANL-0019.md -->
