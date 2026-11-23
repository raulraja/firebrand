---
predictable: spec
---
## Specification Details
- **ID:** SPEC-095
- **Name:** org/firebrandocm/dao/events/ColumnEvent.java

### Description
`ColumnEvent.java` — Column event. This project's call graph records DIRECT calls only, so a function passed to a container, destructured into an exported binding, or reached through a dynamic lookup is not one it can see. Within that limit it records no call to this module. At least one of its operations is exported. `ColumnEvent` carries `persistenceFactory`, `event`, `entity`, `property`, `key`, `columnFamily` and `column`. No requirements recorded yet — 7 operations were examined and no obligation was decided about them.

### Types

`ColumnEvent` — Declares 7 operations:
- `getColumn`() — no requirement inferred
- `getColumnFamily`() — no requirement inferred
- `getEntity`() — no requirement inferred
- `getEvent`() — no requirement inferred
- `getKey`() — no requirement inferred
- `getPersistenceFactory`() — no requirement inferred
- `getProperty`() — no requirement inferred

### Notation

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name.
