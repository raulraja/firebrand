rule "abstractPersistenceFactory_convertWrite_ensures_value_null_value_getclass_null_converter_null"
  tier: pure
  effect: pure
  given:
  when: call precondition "value == null || value.getClass() == null || converter != null"
  then:
  contracts:
    pre: call ensures "value == null || value.getClass() == null || converter != null"
  examples: