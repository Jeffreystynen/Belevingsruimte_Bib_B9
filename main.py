import geluid
import beeld
import threading
import verlichting
import query
import database

audiobooklist = query.audioBook()
soundefectlist = query.soundeffect()
imageslist = query.image()
lightlist = query.light()


# database.create_connection("filename")
audiobook = threading.Thread(target=geluid.sound, args=(audiobooklist,))
soundeffects = threading.Thread(target=geluid.sound, args=(soundefectlist,))
images = threading.Thread(target=beeld.window, args=(imageslist,))
light = threading.Thread(target=verlichting.licht, args=(lightlist,))
databank = threading.Thread(target=database.main)

databank.start()
audiobook.start()
soundeffects.start()
images.start()
light.start()