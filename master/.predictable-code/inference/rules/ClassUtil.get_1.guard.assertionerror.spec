rule "classUtil_get_1_guard_assertionerror"
  tier: pure
  effect: pure
  given:
  when: classLoader == null
  then:
    throw "AssertionError"
  examples:
    example "guard trips":
      inputs:
      expected: error "AssertionError"