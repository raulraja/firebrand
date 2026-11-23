rule "classMetadata_getNamedQuery_ensures_query_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "query != null"
  then:
  contracts:
    pre: call ensures "query != null"
  examples: