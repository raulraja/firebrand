rule "classMetadata_initializeNamedQueries_ensures_org_firebrandocm_dao_classmetadata_namedqueries_containskey_query_name"
  tier: pure
  effect: pure
  given:
  when: call precondition "!(org.firebrandocm.dao.ClassMetadata.namedQueries.containsKey(query.name()))"
  then:
  contracts:
    pre: call ensures "!(org.firebrandocm.dao.ClassMetadata.namedQueries.containsKey(query.name()))"
  examples: