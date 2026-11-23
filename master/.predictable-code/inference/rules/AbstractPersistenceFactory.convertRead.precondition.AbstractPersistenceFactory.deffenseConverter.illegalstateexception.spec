rule "abstractPersistenceFactory_convertRead_inherits_AbstractPersistenceFactory_deffenseConverter_illegalstateexception"
  tier: pure
  effect: pure
  given:
  when: call deffenseConverter_would_throw "IllegalStateException"
  then:
    throw "IllegalStateException"
  examples:
    example "caller hits AbstractPersistenceFactory.deffenseConverter guard":
      inputs:
      expected: error "IllegalStateException"