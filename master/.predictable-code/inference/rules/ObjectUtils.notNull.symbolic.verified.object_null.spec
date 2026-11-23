rule "objectUtils_notNull_ensures_object_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "object != null"
  then:
  contracts:
    pre: call ensures "object != null"
  examples: