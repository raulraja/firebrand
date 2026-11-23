rule "drop_build_guard_illegalargumentexception"
  tier: pure
  effect: pure
  given:
  when: type == null
  then:
    throw "IllegalArgumentException"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalArgumentException"