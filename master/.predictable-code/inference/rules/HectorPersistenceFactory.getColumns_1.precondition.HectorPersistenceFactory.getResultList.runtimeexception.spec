rule "hectorPersistenceFactory_getColumns_1_inherits_HectorPersistenceFactory_getResultList_runtimeexception"
  tier: pure
  effect: pure
  given:
  when: call getResultList_would_throw "RuntimeException"
  then:
    throw "RuntimeException"
  examples:
    example "caller hits HectorPersistenceFactory.getResultList guard":
      inputs:
      expected: error "RuntimeException"