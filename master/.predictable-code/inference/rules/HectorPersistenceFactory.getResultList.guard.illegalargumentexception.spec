rule "hectorPersistenceFactory_getResultList_guard_illegalargumentexception"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "IllegalArgumentException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalArgumentException"