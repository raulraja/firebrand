rule "abstractPersistenceFactory_instantiateContainersIfNecessary_inherits_AbstractPersistenceFactory_getInstance_runtimeexception"
  tier: pure
  effect: pure
  given:
  when: call getInstance_would_throw "RuntimeException"
  then:
    throw "RuntimeException"
  examples:
    example "caller hits AbstractPersistenceFactory.getInstance guard":
      inputs:
      expected: error "RuntimeException"