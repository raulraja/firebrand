rule "hectorPersistenceFactory_destroy_inherits_HectorPersistenceFactory_getResultList_runtimeexception"
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