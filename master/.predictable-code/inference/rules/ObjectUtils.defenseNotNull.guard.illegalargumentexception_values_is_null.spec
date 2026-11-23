rule "objectUtils_defenseNotNull_guard_illegalargumentexception_values_is_null"
  tier: pure
  effect: pure
  given:
  when: values == null
  then:
    throw "IllegalArgumentException: values is null"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalArgumentException: values is null"