---
predictable: spec
---
## Specification Details
- **ID:** SPEC-112
- **Name:** org/firebrandocm/dao/ocmcql/CQLMappedEntityValueConverter.java

### Description
`CQLMappedEntityValueConverter.java` — CQL mapped entity value converter. Called from `CQLMappedCollectionValueConverter.applyConverterInternal` and `CQLMappedCollectionValueConverter.convert`, and possibly from places the call graph cannot see. At run time it reaches `AbstractPersistenceFactory` and `ObjectUtils`. `CQLMappedEntityValueConverter` carries `persistenceFactory`. No requirements recorded yet — 2 operations were examined and no obligation was decided about them.

### Types

`CQLMappedEntityValueConverter` — Declares 2 operations: `applyConverter`(`value`) and `convert`(`value`).
