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
    database = "/home/dyn/ps1/Belevingsruimte_Bib_B9/belevings_ruimte.db"

    sql_create_book_table = """ CREATE TABLE IF NOT EXISTS book (
                                        bookId integer PRIMARY KEY,
                                        title text NOT NULL,
                                        audioFilePath text NOT NULL,
                                        coverFilePath text NOT NULL  
                                    ); """

    sql_create_light_table = """CREATE TABLE IF NOT EXISTS light (
                                    lightId integer PRIMARY KEY,
                                    name text NOT NULL,
                                    color text NOT NULL,
                                    bright integer NOT NULL
                                );"""
    
    sql_create_lightBook_table = """CREATE TABLE IF NOT EXISTS lightBook (
                                    bookId integer NOT NULL,
                                    lightId integer NOT NULL,
                                    lightTiming integer NOT NULL,
                                    orderLight integer NOT NULL,
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

    sql_create_soundeffectBook_table = """CREATE TABLE IF NOT EXISTS soundeffectBook (
                                        bookId integer NOT NULL,
                                        soundeffectId integer NOT NULL,
                                        soundeffectTiming integer NOT NULL,
                                        orderSoundeffect integer NOT NULL,
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
                                            REFERENCES image (imageId)
                                        );"""
    # Book table
    sql_insert_book = """INSERT INTO book (bookId, title, audioFilePath, coverFilePath) VALUES (1,'Book Title 1', '/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.mp3', '/path/to/cover1.jpg');"""

    # Light table
    sql_insert_light1 = """INSERT INTO light (lightId, name, color, bright) VALUES (1, 'Light 1', '255,0,0', 1);"""
    sql_insert_light2 = """INSERT INTO light (lightId, name, color, bright) VALUES (2, 'Light 2', '0,0,255', 0.5);"""
    sql_insert_light3 = """INSERT INTO light (lightId, name, color, bright) VALUES (3, 'Light 3', '0,255,0', 0.5);"""



    # LightBook table
    sql_insert_lightbook1 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 1, 5, 1);"""
    sql_insert_lightbook2 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 2, 5, 2);"""
    sql_insert_lightbook3 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 3, 5, 3);"""



    # SoundEffect table
    sql_insert_soundeffect = """INSERT INTO soundeffect (soundeffectId, name, soundeffectFilePath) VALUES (1, 'Sound Effect 1', '/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.mp3');"""

    # SoundEffectBook table
    sql_insert_soundeffectbook = """INSERT INTO soundeffectBook (bookId, soundeffectId, soundeffectTiming, orderSoundeffect) VALUES (1, 1, 5, 1);"""

    # Image table
    sql_insert_image1 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (1, 'image 1', '/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/1.png');"""
    sql_insert_image2 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (2, 'image 1', '/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/1.png');"""
    sql_insert_image3 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (3, 'image 3', '/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/2.jpg');"""

    # ImageBook table
    sql_insert_imagebook1 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 1, 5000, 1);"""
    sql_insert_imagebook2 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 2, 5000, 2);"""
    sql_insert_imagebook3 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 3, 5000, 3);"""



    # create a database connection
    conn = create_connection(database)
    

    cursor = conn.cursor()

    if conn is not None:
        cursor.execute('''DROP TABLE IF EXISTS soundeffectBook''')
        cursor.execute('''DROP TABLE IF EXISTS imageBook''')
        cursor.execute('''DROP TABLE IF EXISTS lightBook''')
        cursor.execute('''DROP TABLE IF EXISTS soundeffect''')
        cursor.execute('''DROP TABLE IF EXISTS image''')
        cursor.execute('''DROP TABLE IF EXISTS light''')
        cursor.execute('''DROP TABLE IF EXISTS book''')

        create_table(conn, sql_create_book_table)
        create_table(conn, sql_create_light_table)
        create_table(conn, sql_create_image_table)
        create_table(conn, sql_create_soundeffect_table)
        create_table(conn, sql_create_lightBook_table)
        create_table(conn, sql_create_imageBook_table)
        create_table(conn, sql_create_soundeffectBook_table)
        cursor.execute(sql_insert_image1)
        cursor.execute(sql_insert_image2)
        cursor.execute(sql_insert_image3)
        cursor.execute(sql_insert_light1)
        cursor.execute(sql_insert_light2)
        cursor.execute(sql_insert_light3)
        cursor.execute(sql_insert_book)
        cursor.execute(sql_insert_imagebook1)
        cursor.execute(sql_insert_imagebook2)
        cursor.execute(sql_insert_imagebook3)
        cursor.execute(sql_insert_soundeffect)
        cursor.execute(sql_insert_soundeffectbook)
        cursor.execute(sql_insert_lightbook1)
        cursor.execute(sql_insert_lightbook2)
        cursor.execute(sql_insert_lightbook3)


        conn.commit()
        conn.close()
    else:
        print("Error! cannot create the database connection.")
    

main()