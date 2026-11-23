---
predictable: spec
---
## Specification Details
- **ID:** SPEC-111
- **Name:** org/firebrandocm/dao/ocmcql/CQLMappedCollectionValueConverter.java

### Description
`CQLMappedCollectionValueConverter.java` — CQL mapped collection value converter. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. At run time it reaches `CQLMappedEntityValueConverter`. `CQLMappedCollectionValueConverter` carries `cqlMappedEntityValueConverter`. No requirements recorded yet — 3 operations were examined and no obligation was decided about them.

### Types

`CQLMappedCollectionValueConverter` — Declares 3 operations: `applyConverter`(`value`), `convert`(`value`) and `applyConverterInternal`(`value`) (internal).

### Notation

On the cards: `internal` — nothing outside this file can reach the operation (a `private` member, or a declaration the module does not export), so a requirement here is not addressed to anybody outside it.
