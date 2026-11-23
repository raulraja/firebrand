rule "abstractPersistenceFactory_getInstance_ensures_instance_null_body_failed"
  tier: pure
  effect: pure
  given:
  when: call precondition "instance != null || >=body failed>"
  then:
  contracts:
    pre: call ensures "instance != null || >=body failed>"
  examples: