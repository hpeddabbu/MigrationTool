import pymysql

pymysql.install_as_MySQLdb()


class MysqlConnectionAdaptor(object):
    """
    This class creates database session and return it.
    """
    def __init__(self):
        self.db_session = None

    def init_connection_to_mysql(self):
        print("Hi Welcome, Please Enter Valid credentials.")

        try:

            db = pymysql.connect(user=input("Please enter the Username:"),
                                 password=input("Please enter the password:"),
                                 host=input("Please enter the hostname:"),
                                 db=input("Please enter the database:"))
            self.db_session = db
            # TODO: let's not close this session
            # db.close()
        except:
            print("Failed!!please enter valid credentials")
            self.init_connection_to_mysql()
        print("connection to database is sucessfull")

    @property
    def get_mysql_db_session(self):
        return self.db_session




