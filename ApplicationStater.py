import sys
# from folder.module import classname

from Migration.ConnectionAdaptor import MysqlConnectionAdaptor
from Migration.MetadataAdaptor import MysqlMetadataAdaptor


def main(argv):
    connection_obj = MysqlConnectionAdaptor()
    connection_obj.init_connection_to_mysql()

    session = connection_obj.get_mysql_db_session
    # metadata object
    meta_obj = MysqlMetadataAdaptor(session)
    meta_obj.retrieve_metadata_mysql()


if __name__ == '__main__':
    main(sys.argv)

