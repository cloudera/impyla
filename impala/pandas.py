import pandas as pd

def Cursor2DataFrame(cursor):
    names = [metadata[0] for metadata in cursor.description]
    return pd.DataFrame([dict(zip(names, row)) for row in cursor], columns=names)
