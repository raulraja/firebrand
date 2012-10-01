/*
 * Copyright (C) 2012 47 Degrees, LLC
 * http://47deg.com
 * hello@47deg.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.firebrand.dao.cql.clauses;

import org.apache.commons.lang3.StringUtils;

/**
 * A list of columns as in from columnA..columnZ
 */
public class ColumnRange implements SelectClause {
    /* Fields */

	private String from;
	
	private String to;

    /* Constructors */

	public ColumnRange(String from, String to) {
		this.from = from;
		this.to = to;
	}

    /* Canonical Methods */

	@Override
	public String toString() {
		return String.format("'%s'..'%s'", wrapNullIfNecessary(from), wrapNullIfNecessary(to));
	}
	
	private String wrapNullIfNecessary(String value) {
		return StringUtils.isNotBlank(value) ? value : new String(new byte[0]);
	} 
}
