import logging
import os
import mysql.connector

logging.basicConfig(level=logging.INFO)

CONFIG = {
    "user": os.environ.get("USER"),
    "password": os.environ.get("PASSWORD"),
    "host": os.environ.get("HOST"),
    "port": os.environ.get("PORT"),
    "database": os.environ.get("DATABASE"),
}


def get_db_connection(config, as_dict=False):
    ''' Establish a connection to a MySQL database.
    Returns a connection and a cursor.
    '''
    logging.info(f'Connecting to DB with config: {config}')

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(buffered=True, dictionary=as_dict)
    return conn, cursor


def main():
    conn, cursor = get_db_connection(CONFIG)

    query = 'SHOW DATABASES;'
    cursor.execute(query)
    result = [row for row in cursor]

    logging.info(result)

    
if __name__ == '__main__':
    main()
