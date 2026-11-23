---
predictable: spec
---
## Specification Details
- **ID:** SPEC-007
- **Name:** org/firebrandocm/dao/cql/QueryBuilder.java

### Description
`QueryBuilder.java` — Query builder. Called from `AbstractPersistenceFactory.init` and `Query.buildQuery`, and possibly from places the call graph cannot see. At run time it reaches `ClassUtil`. `QueryBuilder` carries `valueConverters`. Checks: “`QueryBuilder.convert_1` only works when the `length` of `values` is at least 0.” and 1 more. 3 requirements: 1 violated, 2 verified.

### Types

`QueryBuilder` — Declares 58 operations:
- `addConverter`(`position`, `valueConverter`) — no requirement inferred
- `createKeyspace`(`keySpace`, `withStrategyClass`, `strategyOptions`) — no requirement inferred
- `createColumnFamily`(`createColumnFamilyClauses`) — no requirement inferred
- `alterColumnFamily`(`columnFamily`, `alterColumn`) — no requirement inferred
- `select`(`clauses`) — no requirement inferred
- `update`(`clauses`) — no requirement inferred
- `delete`(`clauses`) — no requirement inferred
- `truncate`(`clause`) — no requirement inferred
- `drop`(`clause`) — no requirement inferred
- `createIndex`(`clauses`) — no requirement inferred
- `insert`(`clauses`) — no requirement inferred
- `batch`(`batchCapables`) — no requirement inferred
- `use`(`useClause`) — no requirement inferred
- `count`() — no requirement inferred
- `withStrategyClass`(`replicationStrategyClass`) — no requirement inferred
- `columnDefinitions`(`columnTypes`) — no requirement inferred
- `storageOptions`(`storageOptions`) — no requirement inferred
- `storageOption`(`option`, `value`) — no requirement inferred
- `strategyOptions`(`strategyOptions`) — no requirement inferred
- `strategyOption`(`option`, `value`) — no requirement inferred
- `replicationFactor`(`value`) — no requirement inferred
- `dataCenterName`(`dataCenterName`, `value`) — no requirement inferred
- `writeOptions`(`options`) — no requirement inferred
- `into`(`columns`) — no requirement inferred
- `values`(`values`) — no requirement inferred
- `ttl`(`seconds`) — no requirement inferred
- `timestamp`(`timestamp`) — no requirement inferred
- `primaryKey`(`column`, `dataType`) — no requirement inferred
- `column`(`columns`) — no requirement inferred
- `add`(`column`, `dataType`) — no requirement inferred
- `alter`(`column`, `dataType`) — no requirement inferred
- `indexName`(`indexName`) — no requirement inferred
- `keySpace`(`keySpace`) — no requirement inferred
- `columnFamily`(`columnFamily`) — no requirement inferred
- `onColumnFamily`(`columnFamily`) — no requirement inferred
- `first`(`first`) — no requirement inferred
- `reversed`() — no requirement inferred
- `columns`(`columns`) — no requirement inferred
- `allColumns`() — no requirement inferred
- `columnRange`(`from`, `to`) — no requirement inferred
- `from`(`entityClass`) — no requirement inferred
- `consistency`(`consistencyType`) — no requirement inferred
- `set`(`assignments`) — no requirement inferred
- `assign`(`column`, `value`) — no requirement inferred
- `convert`(`value`) — no requirement inferred
- `where`(`predicates`) — no requirement inferred
- `keyIn`(`values`) — no requirement inferred
- `key`(`value`) — no requirement inferred
- `type`(`classValue`) — no requirement inferred
- `eq`(`column`, `value`) — no requirement inferred
- `lt`(`column`, `value`) — no requirement inferred
- `lte`(`column`, `value`) — no requirement inferred
- `gt`(`column`, `value`) — no requirement inferred
- `gte`(`column`, `value`) — no requirement inferred
- `startAt`(`startKey`) — no requirement inferred
- `range`(`startKey`, `endKey`) — no requirement inferred
- `between`(`column`, `from`, `to`) — no requirement inferred
- `limit`(`limit`) — no requirement inferred

A `[verified]` requirement is one the operation checks itself.

Requires of its callers (2) — a `[verified]` one the operation checks itself, or the analysis proved:
- for `convert_1`: the `length` of `values` is at least 0 [verified]
- for `convert_1`: 0 is at most `i` and `i` is less than the `length` of `values` [verified]

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, violated]` — the analysis found a case where the condition fails.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other one.

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Analysis

#### QueryBuilder.convert_1 <!-- predictable:group -->

##### ANL-0013 [implemented, verified]
`QueryBuilder.convert_1` only works when the `length` of `values` is at least 0.

<!-- predictable:analysis -->

<!-- predictable:subject=QueryBuilder.convert_1 -->

<!-- predictable:vc=il1.negative-size -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/QueryBuilder.java:299-306](../../../../../src/main/java/org/firebrandocm/dao/cql/QueryBuilder.java#L299-L306)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-007/ANL-0013.md -->

##### ANL-0014 [implemented, verified]
`QueryBuilder.convert_1` only works when 0 is at most `i` and `i` is less than the `length` of `values`.

<!-- predictable:analysis -->

<!-- predictable:subject=QueryBuilder.convert_1 -->

<!-- predictable:vc=il2.bounds -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/QueryBuilder.java:299-306](../../../../../src/main/java/org/firebrandocm/dao/cql/QueryBuilder.java#L299-L306)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-007/ANL-0014.md -->

#### QueryBuilder.addConverter <!-- predictable:group -->

##### ANL-0015 [implemented, violated]
`QueryBuilder.addConverter` is only called when `position` is one of 0 and 1.

<!-- predictable:analysis -->

<!-- predictable:subject=QueryBuilder.addConverter -->
