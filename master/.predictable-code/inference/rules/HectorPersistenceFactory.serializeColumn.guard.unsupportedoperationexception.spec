rule "hectorPersistenceFactory_serializeColumn_guard_unsupportedoperationexception"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "UnsupportedOperationException"
  examples:
    example "guard trips":
      inputs:
      expected: error "UnsupportedOperationException"