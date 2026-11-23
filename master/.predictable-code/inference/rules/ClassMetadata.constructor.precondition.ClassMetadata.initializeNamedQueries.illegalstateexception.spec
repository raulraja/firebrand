rule "classMetadata_constructor_inherits_ClassMetadata_initializeNamedQueries_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: call initializeNamedQueries_would_throw "IllegalStateException"
  then:
    throw "IllegalStateException"
  examples:
    example "caller hits ClassMetadata.initializeNamedQueries guard":
      inputs:
      expected: error "IllegalStateException"