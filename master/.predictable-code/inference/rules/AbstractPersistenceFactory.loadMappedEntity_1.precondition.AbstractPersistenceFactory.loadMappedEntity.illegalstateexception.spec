rule "abstractPersistenceFactory_loadMappedEntity_1_inherits_AbstractPersistenceFactory_loadMappedEntity_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: call loadMappedEntity_would_throw "IllegalStateException"
  then:
    throw "IllegalStateException"
  examples:
    example "caller hits AbstractPersistenceFactory.loadMappedEntity guard":
      inputs:
      expected: error "IllegalStateException"