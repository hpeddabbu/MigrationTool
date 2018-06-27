# add interpreter pymongo
import pymongo

#from pymongo import MongoClient


class ConnectionMongodb(object):
    """
    Class is for connecting to mongoDB
    """
    def __init__(self, mongo_session):
        self.mongo_session = None

    def init_connection_mongo(self):
        try:

           conn = pymongo.MongoClient('localhost', 27017)
           print("connected successfully")

           self.mongo_session = conn
        except:
            print("Connection Failed! try again")
            self.init_connection_mongo()
        print("connection to db successful")

    @property
    def get_mongo_session(self):
        return self.mongo_session()


class MetaMongodb(object):
    """
    This class is for getting meta data from the database
    """
    # we are now connected to the server
    # mongodb creates databses and collections automatically for you.
    db =conn.mydb
    # viewing database
    db = conn['pro_db']
    # to know what databses are available
    conn.database_names()
    # to view the collections
    db.collection_names()






