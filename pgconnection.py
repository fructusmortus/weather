import psycopg2


def get_connection(dbname):

    connect_str = "dbname={} host='localhost' user='postgres' password='123QWEasd'".format(dbname)

    return psycopg2.connect(connect_str)
