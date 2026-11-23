rule "objectUtils_getAllMethodsInHierarchy_ensures_the_size_must_not_be_negative"
  tier: pure
  effect: pure
  given:
  when: call precondition "The size must not be negative."
  then:
  contracts:
    pre: call ensures "The size must not be negative."
  examples: