---
predictable: spec
---
## Specification Details
- **ID:** SPEC-004
- **Name:** org/firebrandocm/dao/utils/ClassUtil.java

### Description
`ClassUtil.java` — Class util. Called from `AbstractPersistenceFactory.setEntitiesPkg`, `QueryBuilder.columnFamily_1`, `QueryBuilder.from` and `QueryBuilder.onColumnFamily_1`, and possibly from places the call graph cannot see. `findClasses` has 2 failure conditions and 1 of them is stated here — the rest are in the findings in Predictable Code (the Control Center, or your editor). Checks: “`get` throws `AssertionError` unless `classLoader` is not null.” 2 requirements: 1 violated, 1 verified. 1 stated failure.

### Types

`ClassUtil` — Declares 3 operations:
- `get`(`packageName`) — “Scans all classes accessible from the context class loader which belong to the given package and subpackages.” — no requirement inferred
- `findClasses`(`directory`, `packageName`, `annotation`) — “Recursive method used to find all classes in a given directory and subdirs.” — can fail with the error `AssertionError` — one of 2 conditions under which `findClasses` fails, and the only one stated here
- `getColumnFamilyName`(`entityClass`) — “Resolves the physical column family name for this class by checking for a @ColumnFamily(name = ) annotation.” — What `getAnnotation` returns can be null here

A `[verified]` requirement is one the operation checks itself.

Requires of its callers (1) — a `[verified]` one the operation checks itself, or the analysis proved:
- for `get_1`: `classLoader` is not null [verified]

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, violated]` — the analysis found a case where the condition fails.
`[implemented, stated-failure]` — the operation is stated to fail with a named error — a behaviour it has, and one this analysis did not settle as prevented.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other 2.

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Requirements

#### ClassUtil.findClasses <!-- predictable:group -->

`ClassUtil.findClasses` — “Recursive method used to find all classes in a given directory and subdirs.”

##### REQ-0001 [implemented, stated-failure]
Calling `findClasses` can fail with the error `AssertionError`.

<!-- predictable:inferred -->

<!-- predictable:subject=ClassUtil.findClasses -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ClassUtil.java:68-91](../../../../../src/main/java/org/firebrandocm/dao/utils/ClassUtil.java#L68-L91)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-004/REQ-0001.md -->

### Analysis

#### ClassUtil.get_1 <!-- predictable:group -->

##### ANL-0026 [implemented, verified]
`get` throws `AssertionError` unless `classLoader` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassUtil.get_1 -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=AssertionError -->

<!-- predictable:canonical=`ClassUtil.get_1` only works when `classLoader` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ClassUtil.java:43-58](../../../../../src/main/java/org/firebrandocm/dao/utils/ClassUtil.java#L43-L58)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-004/ANL-0026.md -->

### Behaviours

#### ClassUtil.getColumnFamilyName <!-- predictable:group -->

##### BEH-0001 [implemented, violated]
What `getAnnotation` returns can be null here. `getAnnotation` can return nothing in ordinary conditions, and its answer is used without a check, so the first member access throws. Safe to rely on when what `getAnnotation` answers is tested before it is used.

<!-- predictable:behaviour -->

<!-- predictable:subject=ClassUtil.getColumnFamilyName -->

<!-- predictable:vc=site.platform-type-dereferenced.getAnnotation.9f71379d -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ClassUtil.java:102](../../../../../src/main/java/org/firebrandocm/dao/utils/ClassUtil.java#L102)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-004/BEH-0001.md -->
