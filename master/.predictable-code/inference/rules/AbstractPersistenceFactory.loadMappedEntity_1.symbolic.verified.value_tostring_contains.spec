rule "abstractPersistenceFactory_loadMappedEntity_1_ensures_value_tostring_contains"
  tier: pure
  effect: pure
  given:
  when: call precondition "value.toString().contains(\":\")"
  then:
  contracts:
    pre: call ensures "value.toString().contains(\":\")"
  examples: