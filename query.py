import sqlite3
from sqlite3 import Error
import database

db = "/home/dyn/ps1/Belevingsruimte_Bib_B9/belevings_ruimte.db"
 # create a database connection


def soundeffect(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()

    soundeffectList = []
    soundeffectOrder = []
    soundeffectTiming = []
    soundeffectPath = []

    querie = """SELECT sb.orderSoundeffect, sb.soundeffectTiming, s.soundeffectFilePath 
                FROM soundeffectbook sb 
                JOIN soundeffect s ON sb.soundeffectId = s.soundeffectId 
                WHERE sb.bookId = ? 
                ORDER BY sb.orderSoundeffect ASC"""
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
    querie = """SELECT soundFilePath From book
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

    querie = """SELECT lb.orderLight, lb.lightTiming, l.color 
                FROM lightBook lb 
                JOIN light l ON lb.soundeffectId = l.soundeffectId 
                WHERE lb.bookId = ? 
                ORDER BY lb.orderLight ASC"""
    values = (bookId,)

    cursor.execute(querie, values)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        lightOrder.append(row[0])
        lightTiming.append(row[1])
        lightPath.append(row[2])
    
    lightList.append(lightOrder)
    lightList.append(lightTiming)
    lightList.append(lightPath)

    return lightList

def image(bookId):
    global db
    conn = database.create_connection(db)
    cursor = conn.cursor()
    imageList = []
    imageOrder = []
    imageTiming = []
    imagePath = []

    querie = """SELECT ib.orderImage, ib.imageTiming, i.imageFilePath 
                FROM imageBook ib Join image i on i.imageId = ib.imageId 
                where ib.bookId = ? 
                order by ib.orderImage ASC"""
    values = (bookId,)

    cursor.execute(querie, values)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    for row in rows:
        imageOrder.append(row[0])
        imageTiming.append(row[1])
        imagePath.append(row[2])
    
    imageList.append(imageOrder)
    imageList.append(imageTiming)
    imageList.append(imagePath)
    
    return imageList

print(*soundeffect[1])