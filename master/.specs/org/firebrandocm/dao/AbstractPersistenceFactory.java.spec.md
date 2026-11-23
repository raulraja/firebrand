---
predictable: spec
---
## Specification Details
- **ID:** SPEC-001
- **Name:** org/firebrandocm/dao/AbstractPersistenceFactory.java

### Description
`AbstractPersistenceFactory.java` — Abstract persistence factory. Called from `CQLMappedEntityValueConverter.convert`, and possibly from places the call graph cannot see. At run time it reaches 6 other parts of the project. `AbstractPersistenceFactory` carries `MAPPED_ENTITY_VALUE_SEPARATOR`, `MAPPED_VALUE_FORMAT`, `COLLECTION_VALUE_SEPARATOR`, `log`, `typeConverters`, `keyspaceDefinitions`, `entities`, `defaultConsistencyLevel` and 20 more. `getKey` has 4 failure conditions and 2 of them are stated here, `loadMappedCollection` has 3 failure conditions and 1 of them is stated here and `loadMappedEntity` has 3 failure conditions and 1 of them is stated here — the rest are in the findings in Predictable Code (the Control Center, or your editor). REFUTED: “`init` throws `IllegalStateException` unless the value of `getDefaultKeySpace`(the `AbstractPersistenceFactory`) is not null.” 4 requirements: 1 violated, 3 verified. 21 stated failures.

### Types

`AbstractPersistenceFactory` — Declares 55 operations:
- `getContactNodes`() — no requirement inferred
- `setContactNodes`(`contactNodes`) — “Sets the contact nodes.” — no requirement inferred
- `getDefaultConsistencyLevel`() — no requirement inferred
- `setDefaultConsistencyLevel`(`defaultConsistencyLevel`) — “Sets the default consistency level.” — no requirement inferred
- `getDefaultKeySpace`() — no requirement inferred
- `setDefaultKeySpace`(`defaultKeySpace`) — “sets the default keyspace.” — no requirement inferred
- `getPoolName`() — no requirement inferred
- `setPoolName`(`poolName`) — “sets the connection pool name.” — no requirement inferred
- `getThriftPort`() — no requirement inferred
- `setThriftPort`(`thriftPort`) — “Sets the connection thrift port.” — no requirement inferred
- `getTypeConverters`() — “gets the registered type converters.” — no requirement inferred
- `setTypeConverters`(`typeConverters`) — “The type converters map.” — no requirement inferred
- `isDebug`() — no requirement inferred
- `setDebug`(`debug`) — no requirement inferred
- `isDeleteIfNull`() — no requirement inferred
- `setDeleteIfNull`(`deleteIfNull`) — “Sets if deleting when null.” — no requirement inferred
- `isDropOnDestroy`() — “If the factory should drop the keyspace when destroyed.” — no requirement inferred
- `setDropOnDestroy`(`dropOnDestroy`) — “Sets if the factory should drop the keyspace when destroyed.” — no requirement inferred
- `setCleanupDirectories`(`cleanupDirectories`) — “Sets if directories for the embedded server should be deleted.” — no requirement inferred
- `setColumnEventListenerMap`(`columnEventListenerMap`) — “The entity events / listeners map.” — no requirement inferred
- `setDynamicNodeDiscovery`(`dynamicNodeDiscovery`) — “Sets if dynamic node discovery should be enabled.” — no requirement inferred
- `setEmbeddedServerBaseDir`(`embeddedServerBaseDir`) — “Sets The path where the embedded server will be started.” — no requirement inferred
- `setEntities`(`entities`) — “Sets the factory list of entities.” — no requirement inferred
- `setEntitiesPkg`(`entitiesPkg`) — “Sets the factory entities base package.” — no requirement inferred
- `setEntityEventListenerMap`(`entityEventListenerMap`) — “The entity events / listeners map.” — no requirement inferred
- `setReplicaReplacementStrategyClass`(`replicaReplacementStrategyClass`) — “Sets The replica replacement strategy class.” — no requirement inferred
- `setReplicationFactor`(`replicationFactor`) — “Sets the replication factor.” — no requirement inferred
- `setStartEmbeddedServer`(`startEmbeddedServer`) — “sets whether to start the embedded server along with the factory initialization.” — no requirement inferred
- `getManagedClasses`() — “The list of managed class by this factory.” — no requirement inferred
- `addDefaultImplForContainer`(`interfaceClass`, `implClass`) — “Allows external callers to contribute or override the list of default impl for the collection containers.” — no requirement inferred
- `convertWrite`(`value`) — “Converts an object value to a ByteBuffer.” — can fail with "IllegalStateException" unless `value` is null or the value of `getClass`(`value`) is null or `converter` is not null — checked in `AbstractPersistenceFactory.deffenseConverter` [stated-failure]
- `getTypeConverter`(`type`) — “Gets a type converter for a given type.” — no requirement inferred
- `deffenseConverter`(`converter`, `type`) (internal) — “Private helper.” — internal; can fail with the error `IllegalStateException` when `type` is not null and `converter` is null
- `createKeysIfNeeded`(`entities`) — “Creates and assigns set of unique keys.” — no requirement inferred
- `getKey`(`entity`) — “Obtains an entity key.” — can be rejected with the error "IllegalStateException" when `the key property equals null`; can fail with the error `RuntimeException` — one of 4 conditions under which `getKey` fails, and 2 of them are stated here
- `getClassMetadata`(`entityClass`) — “Gets the class metadata from map.” — no requirement inferred
- `getClassMetadataMap`() — “Gets the class metada map.” — no requirement inferred
- `destroy`() — “Destroys this factory instance releasing any resources.” — no requirement inferred
- `fireColumnEvent`(`event`, `entity`, `property`, `key`, `columnFamily`, `column`) — “notifies column event listeners.” — no requirement inferred
- `fireEntityEvent`(`event`, `entities`) — “notifies entity event listeners.” — requires `entities` is null or `entity` is null or `metadata` is null or `listeners` is null [verified]
- `getEntityClassByName`(`entityName`) — “Retrieves an entity class by name.” — no requirement inferred
- `getInstance`(`entityClass`, `instance`) — “Gets a initialized class instance or returns the same instance if not null.” — requires `instance` is not null [verified]
- `getMappedPropertyTokenForPersistentValues`(`value`) — “Gets the mapped property token from a persistent value.”, `getMappedPropertyToken`(`value`, `persist`) (internal) — “Private Helper.”, `getTokenValueForMappedEntity`(`value`) — “Gets a token value from a mapped entity.” — can be rejected with the error "IllegalStateException" — it delegates to `getKey`, which enforces that precondition; can be rejected with the error "RuntimeException" — it delegates to `getKey`, which enforces that precondition
- `initializeMetadata`() — “Initializes metadata.” — no requirement inferred
- `init`() — “Initializes the factory.” — can fail with "IllegalStateException" unless the value of `getDefaultKeySpace`(the `AbstractPersistenceFactory`) is not null — checked in `ObjectUtils.notNull` [violated]
- `initializeKeyspaceDefinitions`() — requires `ksDef` is not null [verified]
- `initializeTypeConverters`() — “Initializes the type converters.” — no requirement inferred
- `instantiateContainersIfNecessary`(`metadata`, `instance`, `name`) — “Instantiates null containers if an association is gonna take place on a mapped property.” — can be rejected with the error "RuntimeException" — it delegates to `getInstance`, which enforces that precondition
- `loadLazyPropertyIfNecessary`(`metadata`, `self`, `proceed`, `m`, `args`) — “To be implemented by subclasses request that a lazy property gets loaded.” — no requirement inferred
- `loadMappedEntity`(`columnValue`) — “Loads a mapped entity.” — can fail with the error `IllegalStateException` — one of 3 conditions under which `loadMappedEntity` fails, and the only one stated here
- `loadProperty`(`metadata`, `name`, `column`) — “Loads a simple, mapped or collection entity property.” — can be rejected with the error "IllegalStateException" — it delegates to `loadMappedEntity`, which enforces that precondition; can be rejected with the error "IllegalStateException" — it delegates to `deffenseConverter`, which enforces that precondition
- `loadMappedCollection`(`column`) — “Loads a mapped collection out of a column.”, `convertRead`(`type`, `value`) — “Converts ByteBuffer to an object value.” — can be rejected with the error "IllegalStateException" — it delegates to `deffenseConverter`, which enforces that precondition

A `[verified]` requirement is one the operation checks itself.

Requires of its callers (1):
- for `loadMappedEntity_1`: `contains`(the value of `toString`(`value`), ":") returns true [stated-failure]

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, violated]` — the analysis found a case where the condition fails.
`[implemented, stated-failure]` — the operation is stated to fail with a named error — a behaviour it has, and one this analysis did not settle as prevented. A row that refuses through a function it calls names it under Enforced by.

**Enforced by** names the function that performs the check, on whatever row carries it: the tag says what the analysis could settle, not whether a check exists.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other 2.

On the cards: `internal` — nothing outside this file can reach the operation (a `private` member, or a declaration the module does not export), so a requirement here is not addressed to anybody outside it. `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Requirements

#### AbstractPersistenceFactory.deffenseConverter <!-- predictable:group -->

`AbstractPersistenceFactory.deffenseConverter` — “Private helper.”

##### REQ-0001 [implemented, stated-failure]
When `type` is not null and `converter` is null, `AbstractPersistenceFactory.deffenseConverter` fails saying "IllegalStateException".

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.deffenseConverter -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:521-527](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L521-L527)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0001.md -->

#### AbstractPersistenceFactory.getInstance_1 <!-- predictable:group -->

##### REQ-0002 [implemented, stated-failure]
Calling `getInstance_1` can fail with the error `IllegalStateException`.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getInstance_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:890-913](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L890-L913)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0002.md -->

##### REQ-0003 [implemented, stated-failure]
Calling `getInstance_1` can fail with the error `RuntimeException`.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getInstance_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:890-913](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L890-L913)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0003.md -->

#### AbstractPersistenceFactory.getKey <!-- predictable:group -->

`AbstractPersistenceFactory.getKey` — “Obtains an entity key.”

##### REQ-0004 [implemented, stated-failure]
When `getKey` is called, if `the key property equals null` then the call is rejected with the error "IllegalStateException".

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getKey -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:569-584](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L569-L584)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0004.md -->

##### REQ-0005 [implemented, stated-failure]
Calling `getKey` can fail with the error `RuntimeException`.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getKey -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:569-584](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L569-L584)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0005.md -->

#### AbstractPersistenceFactory.loadMappedEntity <!-- predictable:group -->

`AbstractPersistenceFactory.loadMappedEntity` — “Loads a mapped entity.”

##### REQ-0006 [implemented, stated-failure]
Calling `loadMappedEntity` can fail with the error `IllegalStateException`.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.loadMappedEntity -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:933-940](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L933-L940)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0006.md -->

#### AbstractPersistenceFactory.convertRead <!-- predictable:group -->

`AbstractPersistenceFactory.convertRead` — “Converts ByteBuffer to an object value.”

##### REQ-0007 [implemented, stated-failure]
Calling `convertRead` can be rejected with the error "IllegalStateException" — it delegates to `deffenseConverter`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.convertRead -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:1013-1017](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L1013-L1017)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0007.md -->

#### AbstractPersistenceFactory.createKeysIfNeeded_1 <!-- predictable:group -->

##### REQ-0008 [implemented, stated-failure]
Calling `createKeysIfNeeded_1` can be rejected with the error "IllegalStateException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.createKeysIfNeeded_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:538-561](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L538-L561)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0008.md -->

##### REQ-0009 [implemented, stated-failure]
Calling `createKeysIfNeeded_1` can be rejected with the error "RuntimeException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.createKeysIfNeeded_1 -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:538-561](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L538-L561)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0009.md -->

#### AbstractPersistenceFactory.getMappedPropertyToken <!-- predictable:group -->

`AbstractPersistenceFactory.getMappedPropertyToken` — “Private Helper.”

##### REQ-0010 [implemented, stated-failure]
Calling `getMappedPropertyToken` can be rejected with the error "IllegalStateException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getMappedPropertyToken -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:739-760](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L739-L760)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0010.md -->

##### REQ-0011 [implemented, stated-failure]
Calling `getMappedPropertyToken` can be rejected with the error "RuntimeException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getMappedPropertyToken -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:739-760](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L739-L760)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0011.md -->

#### AbstractPersistenceFactory.getMappedPropertyTokenForPersistentValues <!-- predictable:group -->

`AbstractPersistenceFactory.getMappedPropertyTokenForPersistentValues` — “Gets the mapped property token from a persistent value.”

##### REQ-0012 [implemented, stated-failure]
Calling `getMappedPropertyTokenForPersistentValues` can be rejected with the error "IllegalStateException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getMappedPropertyTokenForPersistentValues -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:727-729](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L727-L729)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0012.md -->

##### REQ-0013 [implemented, stated-failure]
Calling `getMappedPropertyTokenForPersistentValues` can be rejected with the error "RuntimeException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getMappedPropertyTokenForPersistentValues -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:727-729](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L727-L729)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0013.md -->

#### AbstractPersistenceFactory.getTokenValueForMappedEntity <!-- predictable:group -->

`AbstractPersistenceFactory.getTokenValueForMappedEntity` — “Gets a token value from a mapped entity.”

##### REQ-0014 [implemented, stated-failure]
Calling `getTokenValueForMappedEntity` can be rejected with the error "IllegalStateException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getTokenValueForMappedEntity -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:768-770](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L768-L770)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0014.md -->

##### REQ-0015 [implemented, stated-failure]
Calling `getTokenValueForMappedEntity` can be rejected with the error "RuntimeException" — it delegates to `getKey`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.getTokenValueForMappedEntity -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:768-770](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L768-L770)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0015.md -->

#### AbstractPersistenceFactory.instantiateContainersIfNecessary <!-- predictable:group -->

`AbstractPersistenceFactory.instantiateContainersIfNecessary` — “Instantiates null containers if an association is gonna take place on a mapped property.”

##### REQ-0016 [implemented, stated-failure]
Calling `instantiateContainersIfNecessary` can be rejected with the error "RuntimeException" — it delegates to `getInstance`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.instantiateContainersIfNecessary -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:866-882](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L866-L882)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0016.md -->

#### AbstractPersistenceFactory.loadMappedCollection <!-- predictable:group -->

`AbstractPersistenceFactory.loadMappedCollection` — “Loads a mapped collection out of a column.”

##### REQ-0017 [implemented, stated-failure]
Calling `loadMappedCollection` can be rejected with the error "IllegalStateException" — it delegates to `deffenseConverter`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.loadMappedCollection -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:979-1004](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L979-L1004)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0017.md -->

#### AbstractPersistenceFactory.loadProperty <!-- predictable:group -->

`AbstractPersistenceFactory.loadProperty` — “Loads a simple, mapped or collection entity property.”

##### REQ-0018 [implemented, stated-failure]
Calling `loadProperty` can be rejected with the error "IllegalStateException" — it delegates to `loadMappedEntity`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.loadProperty -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:950-960](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L950-L960)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0018.md -->

##### REQ-0019 [implemented, stated-failure]
Calling `loadProperty` can be rejected with the error "IllegalStateException" — it delegates to `deffenseConverter`, which enforces that precondition.

<!-- predictable:inferred -->

<!-- predictable:subject=AbstractPersistenceFactory.loadProperty -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:950-960](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L950-L960)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/REQ-0019.md -->

### Analysis

#### AbstractPersistenceFactory.convertWrite <!-- predictable:group -->

##### ANL-0001 [implemented, stated-failure]
`convertWrite` throws `IllegalStateException` unless `value` is null or the value of `getClass`(`value`) is null or `converter` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.convertWrite -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalStateException -->

<!-- predictable:canonical=`AbstractPersistenceFactory.convertWrite` only works when `value` is null or the value of `getClass`(`value`) is null or `converter` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:486-495](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L486-L495)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0001.md -->

- **Enforced by:** `AbstractPersistenceFactory.deffenseConverter`

#### AbstractPersistenceFactory.fireEntityEvent <!-- predictable:group -->

##### ANL-0002 [implemented, verified]
`fireEntityEvent` throws `RuntimeException` unless `entities` is null or `entity` is null or `metadata` is null or `listeners` is null.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.fireEntityEvent -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:sibling-vcs=il2.domain-guard -->

<!-- predictable:throws=RuntimeException -->

<!-- predictable:canonical=`AbstractPersistenceFactory.fireEntityEvent` only works when `entities` is null or `entity` is null or `metadata` is null or `listeners` is null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:653-690](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L653-L690)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0002.md -->

#### AbstractPersistenceFactory.getInstance <!-- predictable:group -->

##### ANL-0003 [implemented, verified]
`getInstance` throws `RuntimeException` unless `instance` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.getInstance -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=RuntimeException -->

<!-- predictable:canonical=`AbstractPersistenceFactory.getInstance` only works when `instance` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:710-719](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L710-L719)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0003.md -->

#### AbstractPersistenceFactory.init <!-- predictable:group -->

##### ANL-0004 [implemented, violated]
`init` throws `IllegalStateException` unless the value of `getDefaultKeySpace`(the `AbstractPersistenceFactory`) is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.init -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalStateException -->

<!-- predictable:canonical=`AbstractPersistenceFactory.init` only works when the value of `getDefaultKeySpace`(the `AbstractPersistenceFactory`) is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:793-811](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L793-L811)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0004.md -->

- **Enforced by:** `ObjectUtils.notNull`

#### AbstractPersistenceFactory.initializeKeyspaceDefinitions <!-- predictable:group -->

##### ANL-0005 [implemented, verified]
`AbstractPersistenceFactory.initializeKeyspaceDefinitions` only works when `ksDef` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.initializeKeyspaceDefinitions -->

<!-- predictable:vc=il1.null-dereference -->

<!-- predictable:sibling-vcs=il2.null-dereference il3.null-dereference il4.null-dereference il5.null-dereference -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:813-833](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L813-L833)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0005.md -->

#### AbstractPersistenceFactory.loadMappedEntity_1 <!-- predictable:group -->

##### ANL-0006 [implemented, stated-failure]
`loadMappedEntity` throws `IllegalStateException` unless `contains`(the value of `toString`(`value`), ":") returns true.

<!-- predictable:analysis -->

<!-- predictable:subject=AbstractPersistenceFactory.loadMappedEntity_1 -->

<!-- predictable:vc=il1.domain-guard -->

<!-- predictable:throws=IllegalStateException -->

<!-- predictable:canonical=`AbstractPersistenceFactory.loadMappedEntity_1` only works when `contains`(the value of `toString`(`value`), ":") returns true. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java:968-971](../../../../src/main/java/org/firebrandocm/dao/AbstractPersistenceFactory.java#L968-L971)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-001/ANL-0006.md -->

- **Enforced by:** `AbstractPersistenceFactory.loadMappedEntity`
