rule "drop_build_ensures_type_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "type != null"
  then:
  contracts:
    pre: call ensures "type != null"
  examples: