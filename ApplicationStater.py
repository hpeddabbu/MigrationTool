import sys
# from folder.module import classname

from Migration.ConnectionAdaptor import MysqlConnectionAdaptor
from Migration.MetadataAdaptor import MysqlMetadataAdaptor
from Migration.CoreAdaptor import MysqlCoreAdaptor
from Migration.NosqlConnectionAdaptor import ConnectionMongodb
from Migration.NosqlMetadaAdaptor import MetaMongodb
from Migration.NosqlCoreAdaptor import CoreMongodb

def main(argv):

    # connectionAdaptor object
    connection_obj = MysqlConnectionAdaptor()
    connection_obj.init_connection_to_mysql()
    session = connection_obj.get_mysql_db_session
    # metadata object
    meta_obj = MysqlMetadataAdaptor(session)
    meta_obj.retrieve_metadata_mysql()

    table_name = meta_obj.get_table_name
    field_info = meta_obj.get_field_info
    # core adaptor object
    core_obj = MysqlCoreAdaptor(session, table_name, field_info)
    core_obj.output_data()

    con_obj = ConnectionMongodb()
    con_obj.init_connection_mongo()
    mongo_ses = con_obj.get_mongo_session

    meta_obj = MetaMongodb(mongo_ses, session,table_name, field_info)
    meta_obj.retrieve_metadata_mongodb()
    coll_name =meta_obj.get_collection_name

    core_obj = CoreMongodb(mongo_ses, session,coll_name)
    core_obj.Put_data()


if __name__ == '__main__':
    main(sys.argv)

