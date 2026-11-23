---
predictable: spec
---
## Specification Details
- **ID:** SPEC-009
- **Name:** org/firebrandocm/dao/cql/converters/CQLDateValueConverter.java

### Description
`CQLDateValueConverter.java` — CQL date value converter. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. 1 requirement: 1 verified.

### Types

`CQLDateValueConverter` — Declares 2 operations: `applyConverter`(`value`) and `convert`(`value`).

### Notation

A requirement is a condition an operation needs in order not to fail in the way its own row names — an operation with several failures carries a row for each, and meeting one says nothing about the others. Some a caller supplies, others the operation establishes and checks itself. Nobody has checked the callers.

`implemented` — the operation exists in the code; every machine-written row carries it.

Tags: `[implemented, verified]` — the operation checks this and refuses when it fails.
`[verified]` on the card above and `[implemented, verified]` on a row below are one state. Ids in the machine-managed sections below are assigned per run and are not stable references; cite the requirement's sentence.

### Analysis

#### CQLDateValueConverter.convert <!-- predictable:group -->

##### ANL-0017 [implemented, verified]
The value must denote a number.

<!-- predictable:analysis -->

<!-- predictable:subject=CQLDateValueConverter.convert -->

<!-- predictable:vc=il1.conversion -->

- **Code locations:** [src/main/java/org/firebrandocm/dao/cql/converters/CQLDateValueConverter.java:38-40](../../../../../../src/main/java/org/firebrandocm/dao/cql/converters/CQLDateValueConverter.java#L38-L40)

<!-- predictable:code-locations=.predictable-code/specs/locations/SPEC-009/ANL-0017.md -->
