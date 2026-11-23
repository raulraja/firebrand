rule "cQLDateValueConverter_convert_ensures_the_value_must_denote_a_number"
  tier: pure
  effect: pure
  given:
  when: call precondition "The value must denote a number."
  then:
  contracts:
    pre: call ensures "The value must denote a number."
  examples: