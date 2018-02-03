

class MysqlMetadataAdaptor(object):
    """
    This class connection object and retrieves meta
    data information for core adaptor
    """
    def __init__(self, db_session):
        self._db_session = db_session

    def retrieve_metadata_mysql(self):
        cur = self._db_session.cursor()

        cur.execute('select * from instagram')
        for row in cur.fetchall():
            print(row)
        cur.close()