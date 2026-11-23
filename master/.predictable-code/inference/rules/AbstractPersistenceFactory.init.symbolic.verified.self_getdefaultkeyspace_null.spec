rule "abstractPersistenceFactory_init_ensures_self_getdefaultkeyspace_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "self.getDefaultKeySpace() != null"
  then:
  contracts:
    pre: call ensures "self.getDefaultKeySpace() != null"
  examples: