rule "abstractPersistenceFactory_getTokenValueForMappedEntity_inherits_AbstractPersistenceFactory_getKey_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: call getKey_would_throw "IllegalStateException"
  then:
    throw "IllegalStateException"
  examples:
    example "caller hits AbstractPersistenceFactory.getKey guard":
      inputs:
      expected: error "IllegalStateException"