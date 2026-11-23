---
predictable: spec
---
## Specification Details
- **ID:** SPEC-005
- **Name:** org/firebrandocm/dao/utils/ObjectUtils.java

### Description
`ObjectUtils.java` — Object utils. Called from at least 7 other places in the project. Checks: “`ObjectUtils.defenseNotNull` only works when 0 is at most `i` and `i` is less than the `length` of `values`.” and 3 more. 4 requirements: 4 verified. 2 stated failures.

### Types

`ObjectUtils` — Declares 6 operations:
- `notNull`(`object`, `errorMessage`) — “Ensures an object is not null.” — requires `object` is not null [verified]
- `newTimeUuid`() — “Rerturns a @see UUID based on time.” — no requirement inferred
- `getAllFieldsInHierarchy`(`objectClass`) — “Gets an array of all fields in a class hierarchy walking up to parent classes.” — requires the value of `size`(`allFields`) is at least 0 [verified]
- `getAllMethodsInHierarchy`(`objectClass`) — “Gets an array of all methods in a class hierarchy walking up to parent classes.” — requires the value of `size`(`allMethods`) is at least 0 [verified]
- `defenseNotNull`(`values`) — “Validates that all values are set.” — requires 0 is at most `i` and `i` is less than the `length` of `values` [verified]; can fail with the error "IllegalArgumentException: values is null" when `values` is null; can fail with the error `IllegalArgumentException`
- `getRealClass`(`potentialProxyClass`) — “Gets the real class from a potentially proxied class.” — no requirement inferred

A `[verified]` requirement is one the operation checks itself.

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[implemented, stated-failure]` — the operation is stated to fail with a named error — a behaviour it has, and one this analysis did not settle as prevented.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state;
likewise for the other one.

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Requirements

#### ObjectUtils.defenseNotNull <!-- predictable:group -->

`ObjectUtils.defenseNotNull` — “Validates that all values are set.”

##### REQ-0001 [implemented, stated-failure]
When `values` is null, `ObjectUtils.defenseNotNull` fails saying "IllegalArgumentException: values is null".

<!-- predictable:inferred -->

<!-- predictable:subject=ObjectUtils.defenseNotNull -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:96-106](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L96-L106)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/REQ-0001.md -->

##### REQ-0002 [implemented, stated-failure]
Calling `defenseNotNull` can fail with the error `IllegalArgumentException`.

<!-- predictable:inferred -->

<!-- predictable:subject=ObjectUtils.defenseNotNull -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:96-106](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L96-L106)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/REQ-0002.md -->

### Analysis

#### ObjectUtils.defenseNotNull <!-- predictable:group -->

##### ANL-0027 [implemented, verified]
`ObjectUtils.defenseNotNull` only works when 0 is at most `i` and `i` is less than the `length` of `values`.

<!-- predictable:analysis -->

<!-- predictable:subject=ObjectUtils.defenseNotNull -->

<!-- predictable:vc=il2.bounds -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:96-106](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L96-L106)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/ANL-0027.md -->

#### ObjectUtils.getAllFieldsInHierarchy <!-- predictable:group -->

##### ANL-0028 [implemented, verified]
`ObjectUtils.getAllFieldsInHierarchy` only works when the value of `size`(`allFields`) is at least 0.

<!-- predictable:analysis -->

<!-- predictable:subject=ObjectUtils.getAllFieldsInHierarchy -->

<!-- predictable:vc=il1.negative-size -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:58-70](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L58-L70)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/ANL-0028.md -->

#### ObjectUtils.getAllMethodsInHierarchy <!-- predictable:group -->

##### ANL-0029 [implemented, verified]
`ObjectUtils.getAllMethodsInHierarchy` only works when the value of `size`(`allMethods`) is at least 0.

<!-- predictable:analysis -->

<!-- predictable:subject=ObjectUtils.getAllMethodsInHierarchy -->

<!-- predictable:vc=il1.negative-size -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:77-89](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L77-L89)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/ANL-0029.md -->

#### ObjectUtils.notNull <!-- predictable:group -->

##### ANL-0030 [implemented, verified]
`notNull` throws `IllegalStateException` unless `object` is not null.

<!-- predictable:analysis -->

<!-- predictable:subject=ObjectUtils.notNull -->

<!-- predictable:vc=il1.self-guard -->

<!-- predictable:throws=IllegalStateException -->

<!-- predictable:canonical=`ObjectUtils.notNull` only works when `object` is not null. -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java:41-43](../../../../../src/main/java/org/firebrandocm/dao/utils/ObjectUtils.java#L41-L43)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-005/ANL-0030.md -->
