class MysqlCoreAdaptor:
    """
    This takes the metadata and prints the output to the screen
    """
    def __init__(self, db_session, table_name, field_info):
        self._db_session = db_session
        self.table_name = table_name
        self.field_info = field_info

    def output_data(self):
        cur = self._db_session.cursor()
        fields = ','.join(str(s) for s in self.field_info)

        cur.execute('select ' + fields + ' from ' + self.table_name)

        for row in cur.fetchall():
            print(row)
        cur.close()



