rule "classMetadata_getNamedQuery_guard_illegalargumentexception"
  tier: pure
  effect: pure
  given:
  when: query == null
  then:
    throw "IllegalArgumentException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalArgumentException"