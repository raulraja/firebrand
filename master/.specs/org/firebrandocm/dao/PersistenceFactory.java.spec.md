---
predictable: spec
---
## Specification Details
- **ID:** SPEC-011
- **Name:** org/firebrandocm/dao/PersistenceFactory.java

### Description
`PersistenceFactory.java` — Persistence factory. `PersistenceFactory` declares `deleteColumns`, `executeQuery`, `get`, `getColumns`, `getColumns`, `getDefaultConsistencyLevel`, `getDefaultKeySpace`, `getInstance`, and 7 more (15 in all). No requirements recorded yet.

### Types

`PersistenceFactory` — Declares 14 operations:
- `deleteColumns`(`columnFamily`, `key`, `columns`) — “Deletes columns by name from column family.” — no requirement inferred
- `executeQuery`(`expectedResult`, `query`) — “Executes a query.” — no requirement inferred
- `get`(`entityClass`, `key`) — no requirement inferred
- `getColumns`(`columnFamily`, `key`, `reversed`, `columns`) — “Fetch a map of columns and their values.” — no requirement inferred
- `getDefaultConsistencyLevel`() — no requirement inferred
- `getDefaultKeySpace`() — no requirement inferred
- `getInstance`(`entityClass`) — no requirement inferred
- `getKey`(`entity`) — “Obtains an entity key.” — no requirement inferred
- `getManagedClasses`() — “The list of managed class by this factory.” — no requirement inferred
- `getResultList`(`type`, `query`) — “Get a list of entities given a query.” — no requirement inferred
- `getSingleResult`(`type`, `query`) — “Get a single result from a CQL query.” — no requirement inferred
- `insertColumns`(`columnFamily`, `key`, `keyValuePairs`) — “Inserts columns based on a map representing keys with properties and their corresponding values.” — no requirement inferred
- `persist`(`entities`) — “Entry point method to persist and arbitrary list of objects into the datastore.” — no requirement inferred
- `remove`(`entities`) — no requirement inferred

### Notation

On the cards: `no requirement inferred` — no requirement on this page is about the operation. Either nothing was decided about it, or what was decided is not addressed to a caller (see `internal`); neither means nothing is needed. Where the analysis could not finish, the description above says so by name.
