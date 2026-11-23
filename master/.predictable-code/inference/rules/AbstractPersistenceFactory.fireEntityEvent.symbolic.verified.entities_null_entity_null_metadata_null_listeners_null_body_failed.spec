rule "abstractPersistenceFactory_fireEntityEvent_ensures_entities_null_entity_null_metadata_null_listeners_null_body_failed"
  tier: pure
  effect: pure
  given:
  when: call precondition "entities == null || entity == null || metadata == null || listeners == null || >=body failed>"
  then:
  contracts:
    pre: call ensures "entities == null || entity == null || metadata == null || listeners == null || >=body failed>"
  examples: