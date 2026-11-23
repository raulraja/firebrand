rule "classUtil_get_1_ensures_classloader_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "classLoader != null"
  then:
  contracts:
    pre: call ensures "classLoader != null"
  examples: