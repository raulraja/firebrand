rule "classMetadata_new_requires_target_isannotationpresent"
  tier: pure
  effect: pure
  given:
  when: call precondition "target.isAnnotationPresent(…)"
  then:
    throw "IllegalArgumentException"
  contracts:
    pre: call requires "target.isAnnotationPresent(…)"
  examples: