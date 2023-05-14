import sqlite3
from sqlite3 import Error
import database


db = "/home/dyn/ps1/Belevingsruimte_Bib_B9/belevings_ruimte.db"
 # create a database connection

def books():
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()

    book = []
    

    querie = """SELECT bookId, title, coverFilePath 
                FROM book 
                ORDER BY bookId ASC"""

    cursor.execute(querie)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        bookseperate = []
        bookseperate.append(row[0])
        bookseperate.append(row[1])
        bookseperate.append(row[2])
        book.append(bookseperate)

    return book

def soundeffect(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()

    soundeffectList = []
    soundeffectOrder = []
    soundeffectTiming = []
    soundeffectPath = []

    querie = """SELECT soundeffectbook.orderSoundeffect, soundeffectbook.soundeffectTiming, soundeffect.soundeffectFilePath 
                FROM soundeffectbook 
                JOIN soundeffect ON soundeffectbook.soundeffectId = soundeffect.soundeffectId 
                WHERE soundeffectbook.bookId = ? 
                ORDER BY soundeffectbook.orderSoundeffect ASC"""
    values = (bookId,)

    cursor.execute(querie, values)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        soundeffectOrder.append(row[0])
        soundeffectTiming.append(row[1])
        soundeffectPath.append(row[2])

    soundeffectList.append(soundeffectOrder)
    soundeffectList.append(soundeffectTiming)
    soundeffectList.append(soundeffectPath)

    
    return soundeffectList



def audioBook(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()
    audioBookList = []
    querie = """SELECT audioFilePath From book
                where bookId = ?"""
    values = (bookId,)

    cursor.execute(querie, values)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        audioBookList.append(row)

    return audioBookList

def light(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()
    lightList = []
    lightOrder = []
    lightTiming = []
    lightPath = []
    lightBright = []

    querie = """SELECT lightBook.orderLight, lightBook.lightTiming, light.color, light.bright  
                FROM lightBook
                JOIN light ON lightBook.lightId = light.lightId 
                WHERE lightBook.bookId = ? 
                ORDER BY lightBook.orderLight ASC"""
    values = (bookId,)

    cursor.execute(querie, values)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        lightOrder.append(row[0])
        lightTiming.append(row[1])
        lightPath.append(row[2])
        lightBright.append(row[3])
    
    lightList.append(lightOrder)
    lightList.append(lightTiming)
    lightList.append(lightPath)
    lightList.append(lightBright)


    return lightList

def image(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()
    imageList = []
    imageOrder = []
    imageTiming = []
    imagePath = []

    querie = """SELECT imageBook.orderImage, imageBook.imageTiming, image.imageFilePath 
            FROM imageBook Join image on image.imageId = imageBook.imageId 
            where imageBook.bookId = ?
            order by imageBook.orderImage ASC"""
    values = (bookId,)




    cursor.execute(querie, values)
    rows = cursor.fetchall()
    

    for row in rows:
        imageOrder.append(row[0])
        imageTiming.append(row[1])
        imagePath.append(row[2])
    conn.commit()    
    conn.close()

    imageList.append(imageOrder)
    imageList.append(imageTiming)
    imageList.append(imagePath)
    
    return imageList
