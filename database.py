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
    insert_query_list = []
    # Light table
    sql_insert_light0 = """INSERT INTO light (lightId, name, color, bright) VALUES (1, 'rood', '255,0,0', 1);"""
    sql_insert_light1 = """INSERT INTO light (lightId, name, color, bright) VALUES (2, 'lichtrood', '255,102,102', 1);"""
    sql_insert_light2 = """INSERT INTO light (lightId, name, color, bright) VALUES (3, 'blauw', '0,0,255', 0.5);"""
    sql_insert_light3 = """INSERT INTO light (lightId, name, color, bright) VALUES (4, 'licthblauw', '173,216,230', 1);"""
    sql_insert_light4 = """INSERT INTO light (lightId, name, color, bright) VALUES (5, 'groen', '0,255,0', 0.5);"""
    sql_insert_light5 = """INSERT INTO light (lightId, name, color, bright) VALUES (6, 'licthgroen', '144,238,144', 0.5);"""
    sql_insert_light6 = """INSERT INTO light (lightId, name, color, bright) VALUES (7, 'strandgeel', '248,223,175', 0.5);"""
    insert_query_list.append(sql_insert_light0)
    insert_query_list.append(sql_insert_light1)
    insert_query_list.append(sql_insert_light2)
    insert_query_list.append(sql_insert_light3)
    insert_query_list.append(sql_insert_light4)
    insert_query_list.append(sql_insert_light5)
    insert_query_list.append(sql_insert_light6)

    # Image table
    sql_insert_imageMAIN = """INSERT INTO image (imageId, name, imageFilePath) VALUES (1, 'empty', '');"""
    sql_insert_image0 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (2, 'phone dropped', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/phone-dropped.jpg');"""
    sql_insert_image1 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (3, 'looking at phone', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/lookingphone.jpg');"""
    sql_insert_image2 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (4, 'checkmessages', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/checkmessages.jpg');"""
    sql_insert_image3 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (5, 'frusrtated', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/frustrated.jpg');"""
    sql_insert_image4 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (6, 'plukzelf', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/plukzelf.jpg');"""
    sql_insert_image5 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (7, 'plukwagen', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/rodewagen.webp');"""
    sql_insert_image6 = """INSERT INTO image (imageId, name, imageFilePath) VALUES (8, 'plukhuis', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/images/huis.jpg');"""
    insert_query_list.append(sql_insert_image0)
    insert_query_list.append(sql_insert_image1)
    insert_query_list.append(sql_insert_image2)
    insert_query_list.append(sql_insert_image3)
    insert_query_list.append(sql_insert_image4)
    insert_query_list.append(sql_insert_image5)
    insert_query_list.append(sql_insert_image6)
    insert_query_list.append(sql_insert_imageMAIN)





    # SoundEffect table
    sql_insert_soundeffect0 = """INSERT INTO soundeffect (soundeffectId, name, soundeffectFilePath) VALUES (1, 'spanning', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/soundeffects/spanning.mp3');"""
    sql_insert_soundeffect1 = """INSERT INTO soundeffect (soundeffectId, name, soundeffectFilePath) VALUES (2, 'mysterie', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/soundeffects/mysterie.mp3');"""
    sql_insert_soundeffect2 = """INSERT INTO soundeffect (soundeffectId, name, soundeffectFilePath) VALUES (3, 'kinder', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/soundeffects/kindermuziek.mp3');"""
    insert_query_list.append(sql_insert_soundeffect0)
    insert_query_list.append(sql_insert_soundeffect1)
    insert_query_list.append(sql_insert_soundeffect2)


    # Book table
    sql_insert_book0 = """INSERT INTO book (bookId, title, audioFilePath, coverFilePath) VALUES (1,'Strandfeest', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/audiobook/strandfeest.mp3', 'static/images/strandfeest.jpg');"""
    sql_insert_book1 = """INSERT INTO book (bookId, title, audioFilePath, coverFilePath) VALUES (2,'Pluk', '/home/dyn/ps1/Belevingsruimte_Bib_B9/sources/audiobook/pluk.mp3', 'static/images/pluk.jpg');"""
    insert_query_list.append(sql_insert_book0)
    insert_query_list.append(sql_insert_book1)


    # LightBook table
    sql_insert_lightbook0 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 7, 5, 1);"""
    sql_insert_lightbook1 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 1, 5, 2);"""
    sql_insert_lightbook2 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 7, 5, 3);"""
    sql_insert_lightbook3 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 1, 5, 3);"""
    sql_insert_lightbook4 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 2, 5, 3);"""
    sql_insert_lightbook5 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 4, 5, 3);"""
    sql_insert_lightbook6 = """INSERT INTO lightBook (bookId, lightId, lightTiming, orderLight) VALUES (1, 3, 5, 3);"""

    insert_query_list.append(sql_insert_lightbook0)
    insert_query_list.append(sql_insert_lightbook1)
    insert_query_list.append(sql_insert_lightbook2)
    insert_query_list.append(sql_insert_lightbook3)
    insert_query_list.append(sql_insert_lightbook4)
    insert_query_list.append(sql_insert_lightbook5)
    insert_query_list.append(sql_insert_lightbook6)
    

    # SoundEffectBook table
    sql_insert_soundeffectbook0 = """INSERT INTO soundeffectBook (bookId, soundeffectId, soundeffectTiming, orderSoundeffect) VALUES (1, 2, 1, 1);"""
    sql_insert_soundeffectbook1 = """INSERT INTO soundeffectBook (bookId, soundeffectId, soundeffectTiming, orderSoundeffect) VALUES (1, 1, 1, 2);"""
    sql_insert_soundeffectbook2 = """INSERT INTO soundeffectBook (bookId, soundeffectId, soundeffectTiming, orderSoundeffect) VALUES (2, 3, 1, 1);"""
    insert_query_list.append(sql_insert_soundeffectbook0)
    insert_query_list.append(sql_insert_soundeffectbook1)
    insert_query_list.append(sql_insert_soundeffectbook2)



    
    # ImageBook table
    sql_insert_imagebook0 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 1, 40000, 1);"""
    sql_insert_imagebook2 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 2, 40000, 2);"""
    sql_insert_imagebook3 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 3, 40000, 3);"""
    sql_insert_imagebook4 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 4, 40000, 4);"""
    sql_insert_imagebook5= """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (1, 5, 8000, 5);"""
    sql_insert_imagebook1 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (2, 1, 10000, 1);"""
    sql_insert_imagebook6 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (2, 6, 80000, 2);"""
    sql_insert_imagebook7 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (2, 7, 80000, 3);"""
    sql_insert_imagebook8 = """INSERT INTO imageBook (bookId, imageId, imageTiming, orderImage) VALUES (2, 8, 80000, 4);"""

    insert_query_list.append(sql_insert_imagebook0)
    insert_query_list.append(sql_insert_imagebook1)
    insert_query_list.append(sql_insert_imagebook2)
    insert_query_list.append(sql_insert_imagebook3)
    insert_query_list.append(sql_insert_imagebook4)
    insert_query_list.append(sql_insert_imagebook5)
    insert_query_list.append(sql_insert_imagebook6)
    insert_query_list.append(sql_insert_imagebook7)
    insert_query_list.append(sql_insert_imagebook8)







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
        for insert in insert_query_list:
            cursor.execute(insert)



        conn.commit()
        conn.close()
    else:
        print("Error! cannot create the database connection.")
    

main()