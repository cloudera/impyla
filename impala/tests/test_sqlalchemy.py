from sqlalchemy.engine import create_engine
from sqlalchemy import Table, Column
from sqlalchemy.schema import MetaData, CreateTable

from impala.sqlalchemy import STRING, INT, DOUBLE, TINYINT


def test_sqlalchemy_compilation():
    engine = create_engine('impala://localhost')
    metadata = MetaData(engine)
    # TODO: add other types to this table (e.g., functional.all_types)
    mytable = Table("mytable",
                    metadata,
                    Column('col1', STRING),
                    Column('col2', TINYINT),
                    Column('col3', INT),
                    Column('col4', DOUBLE))
    observed = str(CreateTable(mytable, bind=engine))
    expected = '\nCREATE TABLE mytable (\n\tcol1 STRING, \n\tcol2 TINYINT, \n\tcol3 INT, \n\tcol4 DOUBLE\n)\n\n'
    assert expected == observed
