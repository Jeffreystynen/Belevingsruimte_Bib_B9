import database

conn = database.create_connection('/home/dyn/ps1/belevings_ruimte.db')

def soundeffect():
    soundeffectList = []
    soundeffectOrder = []
    soundeffectTiming = []
    soundeffectPath = []

    rows = database.sql_command(conn, "SELECT * FROM soundeffect")

    for row in rows:
        soundeffectOrder.append(row[0]) # sql query moet 3 rows returnen row 1 = order, 2 = timing, 3 = path
        soundeffectTiming.append(row[1])
        soundeffectPath.append(row[2])

    soundeffectList.append(soundeffectOrder)
    soundeffectList.append(soundeffectTiming)
    soundeffectList.append(soundeffectPath)

    return soundeffectList

def audioBook():
    audioBookList = []
    rows = database.sql_command(conn, "SELECT * FROM audioBook")

    for row in rows:
        audioBookList.append(row)

    return audioBookList

def light():
    lightList = []
    lightOrder = []
    lightTiming = []
    lightPath = []

    rows = database.sql_command(conn, "SELECT * FROM light")

    for row in rows:
        lightOrder.append(row[0])
        lightTiming.append(row[1])
        lightPath.append(row[2])
    
    lightList.append(lightOrder)
    lightList.append(lightTiming)
    lightList.append(lightPath)

    return lightList

def image():
    imageList = []
    imageOrder = []
    imageTiming = []
    imagePath = []

    rows = database.sql_command(conn, "SELECT * FROM image")

    for row in rows:
        imageOrder.append(row[0])
        imageTiming.append(row[1])
        imagePath.append(row[2])
    
    imageList.append(imageOrder)
    imageList.append(imageTiming)
    imageList.append(imagePath)
    
    return imageList

conn.close()
