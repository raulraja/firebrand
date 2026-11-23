rule "hectorPersistenceFactory_init_ensures_self_keyspacedefinitions_size_0"
  tier: pure
  effect: pure
  given:
  when: call precondition "self.keyspaceDefinitions.size() != 0"
  then:
  contracts:
    pre: call ensures "self.keyspaceDefinitions.size() != 0"
  examples: