

class MysqlMetadataAdaptor(object):
    """
    This class connection object and retrieves meta
    data information for core adaptor
    """
    def __init__(self, db_session):
        self._db_session = db_session
        self.table_name = None
        self.field_info = []

    def retrieve_metadata_mysql(self):
        cur = self._db_session.cursor()
        cur.execute('show tables')
        for row in cur.fetchall():
            print(row)

        self.table_name = input("Please choose table_name:")
        cur.execute('Describe ' + self.table_name)
        for row in cur.fetchall():
            self.field_info.append(row[0])

        print(self.field_info)
        cur.close()

    @property
    def get_table_name(self):
        return self.table_name

    @property
    def get_field_info(self):
        return self.field_info

