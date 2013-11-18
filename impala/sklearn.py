from sklearn.base import BaseEstimator


class DataSet(object):
    
    def __init__(self, cursor, query_string, label=None):
        self.cursor = cursor
        self.query_string = query_string






class ImpalaLogisticRegression(BaseEstimator):
    
    def __init__(self, step_size=0.1, mu=0.1):
        self.step_size = step_size
        self.mu = mu
        self.coef_ = None
        return self
    
    def partial_fit(self, cursor, query_string, label_column):
        schema = util.compute_result_schema(cursor, query_string)
        
        if self.coef_ is None:
            self.coef_ = np.zeros()
    
    def fit(self, cursor, query_string, label_column):
        if self.coef_ is None
        "SELECT logr(%(model_state)s,"
                       "%(obs_as_str)s,"
                       "%(label_column)s,
                       "%(step)f, %(mu)f)"


iutil.bismarck_epoch(model_table, dat_table, 'logr(__PREV_MODEL__, %(arr)s, %(label)s, %(step)s, %(mu)s)' % {'arr':arr, 'label':label, 'step':step, 'mu':mu}, epoch, label)

uda_gen = 'logr(__PREV_MODEL__, %(arr)s, %(label)s, %(step)s, %(mu)s)' % {'arr':arr, 'label':label, 'step':step, 'mu':mu}

INSERT INTO model_table
SELECT 5, encodearray(logr(decodearray(model_table.model), toarray(data_table.feat1, data_table.feat2), label, step, mu))
FROM model_table, data_table
WHERE (data_table.label is null || true)=(model_table.model is null || true)
    AND model_table.iter=4;



# TODO
def summarize(cursor, table=None, query_string=None, target_cols=None):
    """Generate summary statistics for a set of rows backed by Impala.
    
    Must provide either the name of a table, or a query that will define the
    table of interest.
    """
    # Ideally, the summarization functionality would be implemented in Impala,
    # allowing for a single pass on the data.  There would be a command like:
    #
    # SELECT summarize(*)
    # FROM
    #     (SELECT * FROM foo);
    #
    # The subquery which defines the rows of interest is provided either as the
    # last executed query in the cursor, as a table name (where we perform
    # SELECT *), or as an arbitrary query of interest
    #
    # The code would look something like this:
    #     summarization_query = "SELECT summarize(*) FROM %s" % query_string
    #     cursor.execute(summarization_query)
    #
    # However for now, we will compute some of these stats by issuing multiple
    # queries.
    
    # determine how the data set of interest is described:
    if table is not None and query_string is None:
        subquery = "SELECT * FROM %s" % table
    elif query_string is not None and table is None:
        subquery = query_string
    else: # query 'preloaded' into cursor
        subquery = cursor.last_query
    
    # get the schema of the data of interest
    if table is not None or query_string is not None:
        # TODO: this is a dirty hack, as a LIMIT clause in subquery will break
        # this. Would be better if Impala had a function I could call for a dry
        # run query
        dry_run_query = '%s LIMIT 0' % subquery
        cursor.execute(dry_run_query)
    schema = cursor.description
    
    # classify the types of the schema
    categoricals = []
    numericals = []
    booleans = []
    for col in schema:
        if col[1] == 'BOOLEAN_TYPE':
            booleans.append(col[0])
        elif col[1] == 'STRING_TYPE':
            categoricals.append(col[0])
        else: # TODO: hopefully numeric
            numericals.append(col[0])
    
    if target_cols is None:
        target_cols = [c[0] for c in schema]
    
    # now to the actual work
    stats = {}
    
    # perform COUNT DISTINCT on the categoricals
    for column in set(target_cols) & set(categoricals):
        count_distinct_query = "SELECT COUNT(DISTINCT %s) FROM %s" % (column, subquery)
        cursor.execute(count_distinct_query)
        distinct = cursor.fetchall()[0][0]
        stats[column] = {'type': 'categorical', 'distinct': distinct}
    
    # compute mean, std for the numerical values
    target_numericals = list(set(target_cols) & set(numericals))
    "SUM(%s), SUM(%s * %s)"
    stats_query = "SELECT "
    
    
    
    
    # COUNT DISTINCT
    
    
