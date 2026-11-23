rule "hectorPersistenceFactory_getColumns_inherits_HectorPersistenceFactory_getResultList_illegalargumentexception"
  tier: pure
  effect: pure
  given:
  when: call getResultList_would_throw "IllegalArgumentException"
  then:
    throw "IllegalArgumentException"
  examples:
    example "caller hits HectorPersistenceFactory.getResultList guard":
      inputs:
      expected: error "IllegalArgumentException"