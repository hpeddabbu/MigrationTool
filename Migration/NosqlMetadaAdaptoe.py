class MetaMongodb(object):
    """
    This class is for getting meta data from the database
    """
    def __init__(self, mongo_session):
        self.mongo_session = mongo_session
        self.collection_name = None
        self.metaField = None

    def retrieve_metadata_mongodb(self):
        # we are now connected to the server
        # mongodb creates databses and collections automatically for you.
        print("hi welcome")
        # db = self.mongo_session.mydb
        #print(db)
        # viewing database

        db = self.mongo_session['local']
        print(db)

        # to know what databases are available
        # db_names = db.database_names()
        # print(db_names)
        # to view the collections
        # collection = db.my_collection
        # print(collection)
        cn = db.collection_names()
        for c in cn:
            print(c)

        col = input("Please select the collection name")
        # Each document in the files collection represents a file in GridFS.
        # to get the meta data
        collection = db[col].find()
        print(collection)
        for item in collection:
            # print(item)
            for key in item.keys():
                print(key)

    @property
    def get_collection_name(self):
        return self.collection_name

    @property
    def get_metafield(self):
        return  self.metaField
