rule "typeConverterSerializer_toByteBuffer_guard_runtimeexception"
  tier: pure
  effect: pure
  given:
  when: true
  then:
    throw "RuntimeException"
  examples:
    example "guard trips":
      inputs:
      expected: error "RuntimeException"