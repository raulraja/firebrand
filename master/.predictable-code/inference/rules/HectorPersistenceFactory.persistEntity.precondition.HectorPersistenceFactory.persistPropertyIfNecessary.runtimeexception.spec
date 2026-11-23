rule "hectorPersistenceFactory_persistEntity_inherits_HectorPersistenceFactory_persistPropertyIfNecessary_runtimeexception"
  tier: pure
  effect: pure
  given:
  when: call persistPropertyIfNecessary_would_throw "RuntimeException"
  then:
    throw "RuntimeException"
  examples:
    example "caller hits HectorPersistenceFactory.persistPropertyIfNecessary guard":
      inputs:
      expected: error "RuntimeException"