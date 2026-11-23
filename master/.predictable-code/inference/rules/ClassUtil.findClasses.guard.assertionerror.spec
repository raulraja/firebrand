rule "classUtil_findClasses_guard_assertionerror"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "AssertionError"
  examples:
    example "guard trips":
      inputs:
      expected: error "AssertionError"