rule "hectorPersistenceFactory_destroy_inherits_HectorPersistenceFactory_getSingleResult_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: call getSingleResult_would_throw "IllegalStateException"
  then:
    throw "IllegalStateException"
  examples:
    example "caller hits HectorPersistenceFactory.getSingleResult guard":
      inputs:
      expected: error "IllegalStateException"