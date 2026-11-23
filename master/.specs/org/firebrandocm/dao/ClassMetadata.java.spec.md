---
predictable: spec
---
## Specification Details
- **ID:** SPEC-002
- **Name:** org/firebrandocm/dao/ClassMetadata.java

### Description
`ClassMetadata.java` — Class metadata. Called from at least 20 other places in the project. At run time it reaches `ObjectUtils`. `ClassMetadata` carries `CLASS_PROPERTY`, `namedQueries`, `log`, `keySpace`, `columnFamily`, `target`, `mutationProperties`, `selectionProperties` and 19 more. Checks: “`getNamedQuery` throws `IllegalArgumentException` unless `query` is not null.” and 2 more. 3 requirements: 3 verified. 4 stated failures.

### Types

`ClassMetadata` — Declares 47 operations:
- `getNamedQuery`(`name`) — “Gets a named query by its name.” — requires `query` is not null [verified]
- `getNullSafeNamedQuery`(`name`) — “Gets a name query by its name returning null if not found.” — no requirement inferred
- `initializeColumnFamilyDefinition`() — “Private helper to initialize a column family definition.” — no requirement inferred
- `processFields`(`target`, `prefix`) — “Processes the target fields searching for persistent annotations.” — no requirement inferred
- `processElement`(`element`, `propertyName`, `type`) — “Processes a field searching for persistent annotations.” — no requirement inferred
- `valid`(`element`, `name`, `type`) — “Private helper.” — no requirement inferred
- `processEmbeddedEntity`(`type`, `propertyName`) — “Processes metadata for a nested embedded association.” — no requirement inferred
- `processMappedEntity`(`type`, `element`, `propertyName`) — “Processes metadata for a nested mapped association.” — no requirement inferred
- `addProperty`(`colAnnotation`, `propertyName`, `type`, `indexed`, `lazy`, `counter`, `counterIncrease`) — “Protected helper that caches information for a property for further persistence consideration.” — no requirement inferred
- `addColumnToColumnFamilyDefinition`(`colAnnotation`, `property`, `indexed`) (internal) — “Private helper that adds a c olumn to a column family definition.” — internal, no requirement inferred
- `isMappedContainer`(`property`) — “Whether this property should be considered as a mapped container which data belongs in some other row.” — no requirement inferred
- `processMappedCollection`(`type`, `element`, `propertyName`) (internal) — “Processes metadata for a nested mapped collection.” — internal, no requirement inferred
- `processCounterIncrease`(`type`, `element`, `propertyName`, `targetCounter`) (internal) — “Processes metadata for counter increase property.” — internal, no requirement inferred
- `processSimpleColumn`(`element`, `propertyName`) — “Processes metadata for a simple column.” — no requirement inferred
- `processMethods`(`target`) (internal) — “Private Helper.” — internal, no requirement inferred
- `processMethod`(`method`) (internal) — “Private Helper.” — internal, no requirement inferred
- `addClassTypePropertyIfSupported`() (internal) — “Private Helper.” — internal, no requirement inferred
- `initializeProxyFactory`(`persistenceFactory`) (internal) — “Initializes a class proxy factory that enhances instances wrapping calls to lazy and other methods that need to be.” — internal, no requirement inferred
- `isLazyAccessor`(`method`) — “Informs whether a method corresponds with a lazy accessor.” — no requirement inferred
- `initializeNamedQueries`(`target`) (internal) — “Private Helper.” — internal; requires `containsKey`(`namedQueries`, the value of `name`(`query`)) returns false [verified]; 0 is at most `i` and `i` is less than the `length` of `value` [verified]
- `getColumnFamily`() — no requirement inferred
- `getColumnFamilyDefinition`() — no requirement inferred
- `getIndexedProperties`() — no requirement inferred
- `getKeyProperty`() — no requirement inferred
- `getKeySpace`() — no requirement inferred
- `getMappedProperties`() — no requirement inferred
- `getMutationProperties`() — no requirement inferred
- `getPropertiesTypesMap`() — no requirement inferred
- `getPropertyContainerMap`() — no requirement inferred
- `getSelectionProperties`() — no requirement inferred
- `getTarget`() — no requirement inferred
- `isCounterColumnFamily`() — no requirement inferred
- `toString`() — no requirement inferred
- `createProxy`() — “Creates a proxy instance for the class represented in this metadata.” — can fail with the error `RuntimeException`
- `destroy`() — “destroys and frees any resources retained by this metadata.” — no requirement inferred
- `getColumnClass`(`name`) — no requirement inferred
- `getLazyProperty`(`method`) — “Gets a lazy property associated to a given a method.” — no requirement inferred
- `getListenersForEvent`(`event`) — “Gets a method associated to a given event.” — no requirement inferred
- `getTargetCounterProperty`(`increaseCounterProperty`) — “Gets a counter property associated to an increase counter property.” — no requirement inferred
- `isContainer`(`property`) — “Checks if a property is a container (embedded, mapped or collection).” — no requirement inferred
- `isAssociationContainer`(`property`) — “Checks if the property is a embedded container.” — no requirement inferred
- `isMappedCollection`(`property`) — “Checks if the property is a mapped collection.” — no requirement inferred
- `isCounterIncreaseProperty`(`property`) — “Checks if the property is a counter increase property.” — no requirement inferred
- `isCounterProperty`(`property`) — “Checks if the property is a counter property.” — no requirement inferred
- `isElementCollection`(`property`) — no requirement inferred
- `isLazyProperty`(`property`) — “Check if the property is flagged as lazy and should be loaded when it's getter is invoked.” — no requirement inferred
- `getConsistencyLevel`() — no requirement inferred

A `[verified]` requirement is one the operation checks itself.

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, stated-failure]` — the operation is stated to fail with a named error — a behaviour it has, and one this analysis did not settle as prevented.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other one.

On the cards: `internal` — nothing outside this file can reach the operation (a `private` member, or a declaration the module does not export), so a requirement here is not addressed to anybody outside it. `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Requirements

#### ClassMetadata.constructor <!-- predictable:group -->

##### REQ-0001 [implemented, stated-failure]
Calling `constructor` can be rejected with the error "IllegalStateException" — it delegates to `initializeNamedQueries`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=ClassMetadata.constructor -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:210-229](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L210-L229)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/REQ-0001.md -->

### Analysis

#### ClassMetadata.constructor <!-- predictable:group -->

##### ANL-0007 [implemented, stated-failure]
Calling `constructor` can fail with the error `IllegalArgumentException`.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.constructor -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalArgumentException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:210-229](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L210-L229)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0007.md -->

#### ClassMetadata.createProxy <!-- predictable:group -->

##### ANL-0008 [implemented, stated-failure]
Calling `createProxy` can fail with the error `RuntimeException`.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.createProxy -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:sibling-vcs=il2.domain-guard -->

<!-- predictable:throws=RuntimeException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:680-691](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L680-L691)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0008.md -->

#### ClassMetadata.getNamedQuery <!-- predictable:group -->

##### ANL-0009 [implemented, verified]
`getNamedQuery` throws `IllegalArgumentException` unless `query` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.getNamedQuery -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalArgumentException -->

<!-- predictable:canonical=`ClassMetadata.getNamedQuery` only works when `query` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:184-189](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L184-L189)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0009.md -->

#### ClassMetadata.initializeNamedQueries <!-- predictable:group -->

##### ANL-0010 [implemented, verified]
`initializeNamedQueries` throws `IllegalStateException` unless `containsKey`(`namedQueries`, the value of `name`(`query`)) returns false.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.initializeNamedQueries -->

<!-- predictable:vc=il2.domain-guard -->

<!-- predictable:throws=IllegalStateException -->

<!-- predictable:canonical=`ClassMetadata.initializeNamedQueries` only works when `containsKey`(`namedQueries`, the value of `name`(`query`)) returns false. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:554-572](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L554-L572)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0010.md -->

##### ANL-0011 [implemented, verified]
`ClassMetadata.initializeNamedQueries` only works when 0 is at most `i` and `i` is less than the `length` of `value`.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.initializeNamedQueries -->

<!-- predictable:vc=il1.bounds -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:554-572](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L554-L572)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0011.md -->

#### ClassMetadata.new <!-- predictable:group -->

##### ANL-0012 [implemented, stated-failure]
Calling `new` can fail with the error `IllegalArgumentException`.

<!-- predictable:analysis -->

<!-- predictable:subject=ClassMetadata.new -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalArgumentException -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/ClassMetadata.java:210-229](../../../../src/main/java/org/firebrandocm/dao/ClassMetadata.java#L210-L229)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-002/ANL-0012.md -->
