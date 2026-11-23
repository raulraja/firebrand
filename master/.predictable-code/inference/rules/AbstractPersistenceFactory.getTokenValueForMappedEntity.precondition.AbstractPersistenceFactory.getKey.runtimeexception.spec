rule "abstractPersistenceFactory_getTokenValueForMappedEntity_inherits_AbstractPersistenceFactory_getKey_runtimeexception"
  tier: pure
  effect: pure
  given:
  when: call getKey_would_throw "RuntimeException"
  then:
    throw "RuntimeException"
  examples:
    example "caller hits AbstractPersistenceFactory.getKey guard":
      inputs:
      expected: error "RuntimeException"