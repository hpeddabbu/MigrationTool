# add interpreter pymongo
from pymongo import MongoClient


class ConnectionMongodb(object):
    """
    Class is for connecting to mongoDB
    """
    def __init__(self):
        self.mongo_session = None

    def init_connection_mongo(self):
        print("MongoAdapter: Please enter login credentials:")
        try:
            conn = MongoClient(host=input("Please enter the hostname:"), port=int(input("Please enter the port no:")))
            print("connected successfully")
            self.mongo_session = conn
        except:
            print("Connection Failed! try again")
            self.init_connection_mongo()
        print("connection to db successful")

    @property
    def get_mongo_session(self):
        return self.mongo_session
