---
predictable: spec
---
## Specification Details
- **ID:** SPEC-110
- **Name:** org/firebrandocm/dao/impl/hector/CqlExecuteQuery.java

### Description
`CqlExecuteQuery.java` — Cql execute query. Called from `HectorPersistenceFactory.getCQLExecuteQuery`, and possibly from places the call graph cannot see. `CqlExecuteQuery` carries `log`, `useCompression` and `query`. No requirements recorded yet — 2 operations were examined and no obligation was decided about them.

### Types

`CqlExecuteQuery` — Declares 3 operations: `execute`(), `setQuery`(`query`) — “Set the query as a String.” and `useCompression`().
