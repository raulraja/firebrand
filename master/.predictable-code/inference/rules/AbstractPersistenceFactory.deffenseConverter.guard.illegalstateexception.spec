rule "abstractPersistenceFactory_deffenseConverter_guard_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: type != null and converter == null
  then:
    throw "IllegalStateException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalStateException"