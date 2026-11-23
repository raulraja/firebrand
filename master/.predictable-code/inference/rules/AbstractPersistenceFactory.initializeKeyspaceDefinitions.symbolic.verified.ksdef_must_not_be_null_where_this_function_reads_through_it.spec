rule "abstractPersistenceFactory_initializeKeyspaceDefinitions_ensures_ksdef_must_not_be_null_where_this_function_reads_through_it"
  tier: pure
  effect: pure
  given:
  when: call precondition "`ksDef` must not be null where this function reads through it."
  then:
  contracts:
    pre: call ensures "`ksDef` must not be null where this function reads through it."
  examples: