class CoreMongodb(object):
    """
    core logic comes here
    """
    def __init__(self,mongo_session, session, coll_name):
        self.mongo_session = mongo_session
        self.session = session
        self.coll_name = coll_name

    def Put_data(self):
        cur = self.session.cursor()
        db_mongo = self.mongo_session['local']
        col = input("Please select the collection name")

        csr = db_mongo.collection21.find({})
        for document in csr:
            print(document)

        cur.close()
