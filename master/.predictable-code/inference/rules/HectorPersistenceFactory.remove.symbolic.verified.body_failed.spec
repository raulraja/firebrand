rule "hectorPersistenceFactory_remove_ensures_body_failed"
  tier: pure
  effect: pure
  given:
  when: call precondition ">=body failed>"
  then:
  contracts:
    pre: call ensures ">=body failed>"
  examples: