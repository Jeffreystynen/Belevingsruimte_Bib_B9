import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    # database = r"pathname
    database = r""
    # create_table("PRAGMA foreign_keys = ON;")

    sql_create_book_table = """ CREATE TABLE IF NOT EXISTS book (
                                        bookId integer PRIMARY KEY,
                                        title text NOT NULL,
                                        audioFilePath text NOT NULL,
                                        coverFilePath text NOT NULL  
                                    ); """

    sql_create_light_table = """CREATE TABLE IF NOT EXISTS light (
                                    lightId integer PRIMARY KEY,
                                    name text NOT NULL,
                                    color text NOT NULL
                                );"""
    
    sql_create_lightBook_table = """CREATE TABLE IF NOT EXISTS lightBook (
                                    bookId integer NOT NULL,
                                    lightId integer NOT NULL,
                                    lightTiming integer NOT NULL,
                                    FOREIGN KEY (bookId)
                                    REFERENCES book(bookId)
                                    FOREIGN KEY (lightId)
                                    REFERENCES light (lightId)
                                );"""

    sql_create_soundeffect_table = """CREATE TABLE IF NOT EXISTS soundeffect (
                                       soundeffectId integer PRIMARY KEY,
                                       name text NOT NULL,
                                       soundeffectFilePath text NOT NULL
                                   );"""

    sql_create_soundeffectBook_table = """CREATE TABLE IF NOT EXISTS soudeffectBook (
                                        bookId integer NOT NULL,
                                        soundeffectId integer NOT NULL,
                                        soundeffectTiming integer NOT NULL,
                                        FOREIGN KEY (bookId)
                                        REFERENCES book(bookId)
                                        FOREIGN KEY (soundeffectId)
                                        REFERENCES soundeffect (soundeffectId)
                                    );"""

    sql_create_image_table = """CREATE TABLE IF NOT EXISTS image (
                                          imageId integer PRIMARY KEY,
                                          name text NOT NULL,
                                          imageFilePath text NOT NULL
                                      );"""

    sql_create_imageBook_table = """CREATE TABLE IF NOT EXISTS imageBook (
                                            bookId integer NOT NULL,
                                            imageId integer NOT NULL,
                                            imageTiming integer NOT NULL,
                                            orderImage integer NOT NULL,
                                            FOREIGN KEY (bookId)
                                            REFERENCES book(bookId)
                                            FOREIGN KEY (imageId)
                                            REFERENCES soundeffect (imageId)
                                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_book_table)
        create_table(conn, sql_create_light_table)
        create_table(conn, sql_create_lightBook_table)
        create_table(conn, sql_create_soundeffect_table)
        create_table(conn, sql_create_soundeffectBook_table)
        create_table(conn, sql_create_image_table)
        create_table(conn, sql_create_imageBook_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()