rule "hectorPersistenceFactory_serializeColumns_inherits_HectorPersistenceFactory_serializeColumn_unsupportedoperationexception"
  tier: pure
  effect: pure
  given:
  when: call serializeColumn_would_throw "UnsupportedOperationException"
  then:
    throw "UnsupportedOperationException"
  examples:
    example "caller hits HectorPersistenceFactory.serializeColumn guard":
      inputs:
      expected: error "UnsupportedOperationException"