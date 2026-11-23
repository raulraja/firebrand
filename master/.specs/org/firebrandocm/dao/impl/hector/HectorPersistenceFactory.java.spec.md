---
predictable: spec
---
## Specification Details
- **ID:** SPEC-003
- **Name:** org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java

### Description
`HectorPersistenceFactory.java` — Hector persistence factory. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. At run time it reaches `ClassMetadata`, `CqlExecuteQuery` and `Query`. `HectorPersistenceFactory` carries `clusterName`, `credentials`, `autoDiscoverHosts`, `cassandraHostConfigurator` and `cluster`; `TypeConverterSerializer` carries `target`; and 1 more shape. `persistPropertyIfNecessary` has 4 failure conditions and 1 of them is stated here — the rest are in the findings in Predictable Code (the Control Center, or your editor). Checks: “`HectorPersistenceFactory.loadLazyPropertyIfNecessary` only works when 0 is at most 0 and 0 is less than the value of `size`(`columns`).” 1 requirement: 1 verified. 36 stated failures.

### Types

`HectorPersistenceFactory` — Declares 35 operations:
- `setAutoDiscoverHosts`(`autoDiscoverHosts`) — “Sets the autoDiscoverHosts property.” — no requirement inferred
- `setCassandraHostConfigurator`(`cassandraHostConfigurator`) — “Sets a cassandra host configurator instance.” — no requirement inferred
- `setClusterName`(`clusterName`) — “Sets the cluster name.” — no requirement inferred
- `setCredentials`(`credentials`) — “Sets the cluster credentials.” — no requirement inferred
- `deleteColumns`(`colFamily`, `key`, `columns`) — “Deletes columns by name from column family.” — no requirement inferred
- `get`(`entityClass`, `key`) — “Get an entity by id.”, `getColumns`(`columnFamily`, `key`, `reversed`, `columns`) — “Fetch a map of columns and their values.”, `destroy`() — “Destroy method that shutdowns this factory.” — can be rejected with the error "IllegalStateException" — it delegates to `getSingleResult`, which enforces that precondition; can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition; can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition; can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition
- `getResultList`(`type`, `query`) — “Get a list of entities given a query.” — can fail with the error `IllegalArgumentException`; can fail with the error `RuntimeException`; can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition
- `getSingleResult`(`type`, `query`) — “Get a single result from a CQL query.” — can fail with the error `IllegalStateException`; can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition; can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition; can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition
- `insertColumns`(`colFamily`, `key`, `keyValuePairs`) — “Inserts columns based on a map representing keys with properties and their corresponding values.” — no requirement inferred
- `persist`(`entities`) — “Entry point method to persist and arbitrary list of objects into the datastore.”, `remove`(`entities`) — “Removes a list of entities from the data store.”, `persistPropertyIfNecessary`(`mutator`, `key`, `classMetadata`, `entity`, `property`) — “helper that persist an entity property.” — can fail with the error `RuntimeException`
- `executeQuery`(`expectedResult`, `query`) — “Executes a query.” — no requirement inferred
- `getCQLExecuteQuery`(`query`) — “Private helper that returns a CqlExecuteQuery.” — no requirement inferred
- `getCQLQuery`(`type`, `query`) — “Private helper to obtain a CqlQuery given an entity class type and a cql query.” — no requirement inferred
- `getDefaultKeyspace`() — internal, no requirement inferred
- `init`() — “Initializes the factory.” — can be rejected with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory" — it delegates to `initializeSchema`, which enforces that precondition; can fail with "no keyspace definitions founds, maybe add some entities to the factory" unless the value of `size`(the `keyspaceDefinitions` of the `HectorPersistenceFactory`) is not equal to 0 — checked in `HectorPersistenceFactory.initializeSchema` [stated-failure]
- `initializeSchema`() — “Private helper to initialize the schema.” — can fail with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"
- `keyspaceContainsColumnFamily`(`columnFamilyDefinition`, `keyspaceDefinition`) — “Private helper to determine if a column family has already been created in a keyspace.” — no requirement inferred
- `getColumnFamilyFromKeyspace`(`name`, `keyspaceDefinition`) — “Private helper to obtain a column family from a keyspace by name.” — no requirement inferred
- `loadLazyPropertyIfNecessary`(`metadata`, `self`, `proceed`, `m`, `args`) — “Loads a lazy property's value.” — requires 0 is at most 0 and 0 is less than the value of `size`(`columns`) [verified]
- `getSliceQuery`(`classMetadata`) (internal) — “Private helper to get a slice query given a class metadata.” — internal, no requirement inferred
- `getKeyspace`(`classMetadata`) (internal) — “Gets a keyspace associated with a class metadata.” — internal, no requirement inferred
- `getColumnFamilyConsistencyLevel`(`classMetadata`) (internal) — “Get the default consistency level for a keyspace given the class metadata.” — internal, no requirement inferred
- `isEmptyContainerValue`(`value`) (internal) — “Private helper to determine if a container is empty.” — internal, no requirement inferred
- `persistAll`(`entities`) (internal) — “private helper to persist and arbitrary list of objects into the datastore.”, `persistEntity`(`entity`) — “helper that persists a single an entity in the data store.” — can be rejected with the error "RuntimeException" — it delegates to `persistPropertyIfNecessary`, which enforces that precondition
- `getMutator`(`classMetadata`) (internal) — “Given a classMetadata obtain a mutator.” — internal, no requirement inferred
- `update`(`mutator`, `key`, `entity`, `property`, `value`) (internal) — “Invoked when a setter is invoked in any entity changing a property value.” — internal, no requirement inferred
- `updateWithMetadata`(`mutator`, `key`, `metadata`, `property`, `value`, `entity`) (internal) — “Private helper that delegates to updateSimpleColumn.” — internal, no requirement inferred
- `updateSimpleColumn`(`mutator`, `key`, `metadata`, `property`, `value`, `entity`) — “Private helper that updates a simple column.” — no requirement inferred
- `serializeColumns`(`key`, `metadata`, `entityClass`, `columns`, `instance`, `ignoreLazyFlags`) (internal) — “Private helper that hidrates an entity from a list of columns in the datastore.” — internal; can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition
- `serializeColumn`(`metadata`, `instance`, `name`, `column`, `ignoreLazyFlags`) — “Private helper that serializes a column to an entity property.” — can fail with the error `UnsupportedOperationException`

A `[verified]` requirement is one the operation checks itself.

`TypeConverterSerializer` — Declares 2 operations:
- `toByteBuffer`(`obj`), `fromByteBuffer`(`byteBuffer`) — can fail with the error `RuntimeException`

A `[verified]` requirement is one the operation checks itself.

`Builder` — Declares 20 operations:
- `autoDiscoverHosts`(`autoDiscoverHosts`) — no requirement inferred
- `clusterName`(`clusterName`) — no requirement inferred
- `credentials`(`credentials`) — no requirement inferred
- `contactNodes`(`contactNodes`) — no requirement inferred
- `defaultConsistencyLevel`(`defaultConsistencyLevel`) — no requirement inferred
- `defaultKeySpace`(`defaultKeySpace`) — no requirement inferred
- `poolName`(`poolName`) — no requirement inferred
- `thriftPort`(`thriftPort`) — no requirement inferred
- `typeConverters`(`typeConverters`) — no requirement inferred
- `debug`(`debug`) — no requirement inferred
- `deleteIfNull`(`deleteIfNull`) — no requirement inferred
- `dropOnDestroy`(`dropOnDestroy`) — no requirement inferred
- `columnEventListenerMap`(`columnEventListenerMap`) — no requirement inferred
- `embeddedServerBaseDir`(`embeddedServerBaseDir`) — no requirement inferred
- `entityEventListenerMap`(`entityEventListenerMap`) — no requirement inferred
- `replicationFactor`(`replicationFactor`) — no requirement inferred
- `startEmbeddedServer`(`startEmbeddedServer`) — no requirement inferred
- `entities`(`entities`) — no requirement inferred
- `cassandraHostConfigurator`(`cassandraHostConfigurator`) — no requirement inferred
- `build`() — can be rejected with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory" — it delegates to `initializeSchema`, which enforces that precondition

A `[verified]` requirement is one the operation checks itself.

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, stated-failure]` — the operation is stated to fail with a named error — a behaviour it has, and one this analysis did not settle as prevented. A row that refuses through a function it calls names it under Enforced by.

**Enforced by** names the function that performs the check, on whatever row carries it: the tag says what the analysis could settle, not whether a check exists.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other one.

On the cards: `internal` — nothing outside this file can reach the operation (a `private` member, or a declaration the module does not export), so a requirement here is not addressed to anybody outside it. `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Requirements

#### HectorPersistenceFactory.getResultList <!-- predictable:group -->

`HectorPersistenceFactory.getResultList` — “Get a list of entities given a query.”

##### REQ-0001 [implemented, stated-failure]
Calling `getResultList` can fail with the error `IllegalArgumentException`.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getResultList -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:217-247](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L217-L247)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0001.md -->

##### REQ-0002 [implemented, stated-failure]
Calling `getResultList` can fail with the error `RuntimeException`.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getResultList -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:217-247](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L217-L247)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0002.md -->

##### REQ-0024 [implemented, stated-failure]
Calling `getResultList` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getResultList -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:217-247](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L217-L247)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0024.md -->

#### HectorPersistenceFactory.getSingleResult <!-- predictable:group -->

`HectorPersistenceFactory.getSingleResult` — “Get a single result from a CQL query.”

##### REQ-0003 [implemented, stated-failure]
Calling `getSingleResult` can fail with the error `IllegalStateException`.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getSingleResult -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:258-264](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L258-L264)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0003.md -->

##### REQ-0025 [implemented, stated-failure]
Calling `getSingleResult` can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getSingleResult -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:258-264](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L258-L264)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0025.md -->

##### REQ-0026 [implemented, stated-failure]
Calling `getSingleResult` can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getSingleResult -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:258-264](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L258-L264)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0026.md -->

##### REQ-0027 [implemented, stated-failure]
Calling `getSingleResult` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getSingleResult -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:258-264](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L258-L264)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0027.md -->

#### HectorPersistenceFactory.initializeSchema <!-- predictable:group -->

`HectorPersistenceFactory.initializeSchema` — “Private helper to initialize the schema.”

##### REQ-0004 [implemented, stated-failure]
Calling `initializeSchema` can fail with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory".

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.initializeSchema -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:453-477](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L453-L477)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0004.md -->

#### HectorPersistenceFactory.persistPropertyIfNecessary <!-- predictable:group -->

`HectorPersistenceFactory.persistPropertyIfNecessary` — “helper that persist an entity property.”

##### REQ-0005 [implemented, stated-failure]
Calling `persistPropertyIfNecessary` can fail with the error `RuntimeException`.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.persistPropertyIfNecessary -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:641-676](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L641-L676)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0005.md -->

#### HectorPersistenceFactory.serializeColumn <!-- predictable:group -->

`HectorPersistenceFactory.serializeColumn` — “Private helper that serializes a column to an entity property.”

##### REQ-0006 [implemented, stated-failure]
Calling `serializeColumn` can fail with the error `UnsupportedOperationException`.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.serializeColumn -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:774-789](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L774-L789)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0006.md -->

#### Builder.build <!-- predictable:group -->

##### REQ-0007 [implemented, stated-failure]
Calling `build` can be rejected with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory" — it delegates to `initializeSchema`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=Builder.build -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:958-961](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L958-L961)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0007.md -->

#### HectorPersistenceFactory.destroy <!-- predictable:group -->

`HectorPersistenceFactory.destroy` — “Destroy method that shutdowns this factory.”

##### REQ-0008 [implemented, stated-failure]
Calling `destroy` can be rejected with the error "IllegalStateException" — it delegates to `getSingleResult`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.destroy -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:343-349](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L343-L349)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0008.md -->

##### REQ-0009 [implemented, stated-failure]
Calling `destroy` can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.destroy -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:343-349](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L343-L349)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0009.md -->

##### REQ-0010 [implemented, stated-failure]
Calling `destroy` can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.destroy -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:343-349](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L343-L349)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0010.md -->

##### REQ-0011 [implemented, stated-failure]
Calling `destroy` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.destroy -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:343-349](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L343-L349)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0011.md -->

#### HectorPersistenceFactory.get <!-- predictable:group -->

`HectorPersistenceFactory.get` — “Get an entity by id.”

##### REQ-0012 [implemented, stated-failure]
Calling `get` can be rejected with the error "IllegalStateException" — it delegates to `getSingleResult`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.get -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:164-171](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L164-L171)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0012.md -->

##### REQ-0013 [implemented, stated-failure]
Calling `get` can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.get -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:164-171](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L164-L171)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0013.md -->

##### REQ-0014 [implemented, stated-failure]
Calling `get` can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.get -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:164-171](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L164-L171)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0014.md -->

##### REQ-0015 [implemented, stated-failure]
Calling `get` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.get -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:164-171](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L164-L171)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0015.md -->

#### HectorPersistenceFactory.getColumns <!-- predictable:group -->

`HectorPersistenceFactory.getColumns` — “Fetch a map of columns and their values.”

##### REQ-0016 [implemented, stated-failure]
Calling `getColumns` can be rejected with the error "IllegalStateException" — it delegates to `getSingleResult`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:183-187](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L183-L187)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0016.md -->

##### REQ-0017 [implemented, stated-failure]
Calling `getColumns` can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:183-187](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L183-L187)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0017.md -->

##### REQ-0018 [implemented, stated-failure]
Calling `getColumns` can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:183-187](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L183-L187)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0018.md -->

##### REQ-0019 [implemented, stated-failure]
Calling `getColumns` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:183-187](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L183-L187)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0019.md -->

#### HectorPersistenceFactory.getColumns_1 <!-- predictable:group -->

##### REQ-0020 [implemented, stated-failure]
Calling `getColumns_1` can be rejected with the error "IllegalStateException" — it delegates to `getSingleResult`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:201-205](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L201-L205)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0020.md -->

##### REQ-0021 [implemented, stated-failure]
Calling `getColumns_1` can be rejected with the error "IllegalArgumentException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:201-205](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L201-L205)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0021.md -->

##### REQ-0022 [implemented, stated-failure]
Calling `getColumns_1` can be rejected with the error "RuntimeException" — it delegates to `getResultList`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:201-205](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L201-L205)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0022.md -->

##### REQ-0023 [implemented, stated-failure]
Calling `getColumns_1` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.getColumns_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:201-205](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L201-L205)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0023.md -->

#### HectorPersistenceFactory.init <!-- predictable:group -->

`HectorPersistenceFactory.init` — “Initializes the factory.”

##### REQ-0028 [implemented, stated-failure]
Calling `init` can be rejected with the error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory" — it delegates to `initializeSchema`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.init -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:433-448](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L433-L448)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0028.md -->

#### HectorPersistenceFactory.persistAll <!-- predictable:group -->

`HectorPersistenceFactory.persistAll` — “private helper to persist and arbitrary list of objects into the datastore.”

##### REQ-0029 [implemented, stated-failure]
Calling `persistAll` can be rejected with the error "RuntimeException" — it delegates to `persistPropertyIfNecessary`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.persistAll -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:595-601](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L595-L601)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0029.md -->

#### HectorPersistenceFactory.persistEntity <!-- predictable:group -->

`HectorPersistenceFactory.persistEntity` — “helper that persists a single an entity in the data store.”

##### REQ-0030 [implemented, stated-failure]
Calling `persistEntity` can be rejected with the error "RuntimeException" — it delegates to `persistPropertyIfNecessary`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.persistEntity -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:608-618](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L608-L618)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0030.md -->

#### HectorPersistenceFactory.serializeColumns <!-- predictable:group -->

`HectorPersistenceFactory.serializeColumns` — “Private helper that hidrates an entity from a list of columns in the datastore.”

##### REQ-0031 [implemented, stated-failure]
Calling `serializeColumns` can be rejected with the error "UnsupportedOperationException" — it delegates to `serializeColumn`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=HectorPersistenceFactory.serializeColumns -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:755-763](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L755-L763)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/REQ-0031.md -->

### Analysis

#### TypeConverterSerializer.fromByteBuffer <!-- predictable:group -->

##### ANL-0020 [implemented, stated-failure]
Calling `fromByteBuffer` can fail with the error `RuntimeException`.

<!-- predictable:analysis -->

<!-- predictable:subject=TypeConverterSerializer.fromByteBuffer -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=RuntimeException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:843-849](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L843-L849)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0020.md -->

#### TypeConverterSerializer.toByteBuffer <!-- predictable:group -->

##### ANL-0021 [implemented, stated-failure]
Calling `toByteBuffer` can fail with the error `RuntimeException`.

<!-- predictable:analysis -->

<!-- predictable:subject=TypeConverterSerializer.toByteBuffer -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=RuntimeException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:830-836](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L830-L836)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0021.md -->

#### HectorPersistenceFactory.init <!-- predictable:group -->

##### ANL-0022 [implemented, stated-failure]
`init` fails with "no keyspace definitions founds, maybe add some entities to the factory" unless the value of `size`(the `keyspaceDefinitions` of the `HectorPersistenceFactory`) is not equal to 0.

<!-- predictable:analysis -->

<!-- predictable:subject=HectorPersistenceFactory.init -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=no keyspace definitions founds, maybe add some entities to the factory -->

<!-- predictable:canonical=`HectorPersistenceFactory.init` only works when the value of `size`(the `keyspaceDefinitions` of the `HectorPersistenceFactory`) is not equal to 0. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:433-448](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L433-L448)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0022.md -->

- **Enforced by:** `HectorPersistenceFactory.initializeSchema`

#### HectorPersistenceFactory.loadLazyPropertyIfNecessary <!-- predictable:group -->

##### ANL-0023 [implemented, verified]
`HectorPersistenceFactory.loadLazyPropertyIfNecessary` only works when 0 is at most 0 and 0 is less than the value of `size`(`columns`).

<!-- predictable:analysis -->

<!-- predictable:subject=HectorPersistenceFactory.loadLazyPropertyIfNecessary -->

<!-- predictable:vc=il1.bounds -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:525-541](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L525-L541)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0023.md -->

#### HectorPersistenceFactory.persist <!-- predictable:group -->

##### ANL-0024 [implemented, stated-failure]
Calling `persist` can fail with the error `RuntimeException`.

<!-- predictable:analysis -->

<!-- predictable:subject=HectorPersistenceFactory.persist -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:sibling-vcs=il2.domain-guard il3.domain-guard -->

<!-- predictable:throws=RuntimeException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:294-306](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L294-L306)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0024.md -->

#### HectorPersistenceFactory.remove <!-- predictable:group -->

##### ANL-0025 [implemented, stated-failure]
Calling `remove` can fail with the error `RuntimeException`.

<!-- predictable:analysis -->

<!-- predictable:subject=HectorPersistenceFactory.remove -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=RuntimeException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java:313-334](../../../../../../src/main/java/org/firebrandocm/dao/impl/hector/HectorPersistenceFactory.java#L313-L334)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-003/ANL-0025.md -->
