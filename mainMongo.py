import sys

from Migration.NosqlConnectionAdaptor import ConnectionMongodb
from Migration.NosqlMetadaAdaptoe import MetaMongodb


def mainMangodb(argv):
    con_obj = ConnectionMongodb()
    con_obj.init_connection_mongo()
    mongo_ses = con_obj.get_mongo_session

    meta_obj = MetaMongodb(mongo_ses)
    meta_obj.retrieve_metadata_mongodb()


if __name__ == '__main__':
    mainMangodb(sys.argv)