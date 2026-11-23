---
predictable: spec
---
## Specification Details
- **ID:** SPEC-012
- **Name:** org/firebrandocm/dao/Query.java

### Description
`Query.java` — Query. Called from at least 7 other places in the project. At run time it reaches `ClassMetadata` and `QueryBuilder`. `Query` carries `log`, `query` and `params`. No requirements recorded yet — 3 operations were examined and no obligation was decided about them.

### Types

`Query` — Declares 3 operations: `get`(`query`), `buildQuery`(`query`) and `getQuery`().
