rule "abstractPersistenceFactory_getKey_guard_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: keyProperty == null
  then:
    throw "IllegalStateException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalStateException"