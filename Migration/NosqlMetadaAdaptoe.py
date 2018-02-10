class MetaMongodb(object):
    """
    This class is for getting meta data from the database
    """

    def __init__(self, mongo_session,session,table_name, field_info):
        self.mongo_session = mongo_session
        self.session = session
        self.table_name = table_name
        self.field_info = field_info
        self.collection_name = None
        self.metaField = None

    def retrieve_metadata_mongodb(self):
        # we are now connected to the server
        # mongodb creates databses and collections automatically for you.
        print("hi welcome")
        # db = self.mongo_session.mydb
        #print(db)
        # viewing database



        cur = self.session.cursor()

        db_mongo = self.mongo_session['local']
        print(db_mongo)

        fields = ','.join(str(s) for s in self.field_info)
        print(fields)
        cur.execute('select ' + fields + ' from ' + self.table_name)
        row_titles = self.field_info

        # mongo client specifically requires python dict
        cus = dict()

        # custom record id rather than mongodb default hash id
        cid = 0

        # cycle through each mySQL row
        for (row) in cur:
            cid += 1  # increment id
            cus['_id'] = cid

            # check if current row is null
            for i in range(0, len(row)):
                if row[i] == None:
                    # if the record is null, skip it
                    continue
                else:
                    # conversion to string
                    row_title = "".join(row_titles[i])
                    # conversion to string
                    field = str(row[i])

                    # add current record's field's title and value
                    cus[row_title] = field

            # we've completed processing this row, insert it into mongoldb
            id = db_mongo.collection11.insert_one(cus).inserted_id

        cn = db_mongo.collection_names()
        for c in cn:
            print(c)

        col = input("Please select the collection name")

        csr = db_mongo.collection11.find({})
        for document in csr:
            print(document)
            # just for debug purposes, show me running row count
            #print(id)

            # shut down the mysql connection


        # to know what databases are available
        # db_names = db.database_names()
        # print(db_names)
        # to view the collections
        # collection = db.my_collection
        # print(collection)

        # Each document in the files collection represents a file in GridFS.
        # to get the meta data
        """collection = db_mongo[col].find().pretty()
        print(collection)
        for item in collection:
            # print(item)
            for key in item.keys():
                print(key)"""
        cur.close()

    @property
    def get_collection_name(self):
        return self.collection_name

    @property
    def get_metafield(self):
        return  self.metaField
