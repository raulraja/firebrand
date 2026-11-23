rule "classMetadata_initializeNamedQueries_ensures_the_index_must_be_within_the_bounds_of_what_it_indexes"
  tier: pure
  effect: pure
  given:
  when: call precondition "The index must be within the bounds of what it indexes."
  then:
  contracts:
    pre: call ensures "The index must be within the bounds of what it indexes."
  examples: