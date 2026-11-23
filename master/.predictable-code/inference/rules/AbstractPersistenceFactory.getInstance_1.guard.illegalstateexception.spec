rule "abstractPersistenceFactory_getInstance_1_guard_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "IllegalStateException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalStateException"