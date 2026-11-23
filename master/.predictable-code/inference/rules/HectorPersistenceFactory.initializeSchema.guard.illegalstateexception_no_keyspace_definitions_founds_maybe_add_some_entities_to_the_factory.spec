rule "hectorPersistenceFactory_initializeSchema_guard_illegalstateexception_no_keyspace_definitions_founds_maybe_add_some_entities_to_the_factory"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"
  examples:
    example "guard trips":
      inputs:
      expected: error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"