def TRowSet2DataFrame(row_set, schema):
    # TODO: this should be Cythoned
    # TODO: this should be factored into a separate interface
    # row_set is TRowSet
    # schema is TTableSchema
    
    # compute the sequence of type accesses
    names = [col_schema.columnName for col_schema in schema.columns]
    getters = [type_getters[col_schema.typeDesc.types[0].primitiveEntry.type]
            for col_schema in schema.columns]
    
    rows_list = []
    for thrift_row in row_set.rows:
        row_dict = {}
        for (i, col_val) in enumerate(thrift_row.colVals):
            row_dict[names[i]] = getters[i](col_val).value
        rows_list.append(row_dict)
    
    return pd.DataFrame(rows_list, columns=names)