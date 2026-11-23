rule "objectUtils_notNull_guard_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: object == null
  then:
    throw "IllegalStateException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalStateException"