rule "hectorPersistenceFactory_init_inherits_HectorPersistenceFactory_initializeSchema_illegalstateexception_no_keyspace_definitions_founds_maybe_add_some_entities_to_the_factory"
  tier: pure
  effect: pure
  given:
  when: call initializeSchema_would_throw "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"
  then:
    throw "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"
  examples:
    example "caller hits HectorPersistenceFactory.initializeSchema guard":
      inputs:
      expected: error "IllegalStateException: no keyspace definitions founds, maybe add some entities to the factory"