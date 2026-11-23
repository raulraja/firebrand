rule "classUtil_get_1_inherits_ClassUtil_findClasses_assertionerror"
  tier: pure
  effect: pure
  given:
  when: call findClasses_would_throw "AssertionError"
  then:
    throw "AssertionError"
  examples:
    example "caller hits ClassUtil.findClasses guard":
      inputs:
      expected: error "AssertionError"