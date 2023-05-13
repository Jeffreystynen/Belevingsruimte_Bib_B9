import geluid
import beeld
import threading
import verlichting
import query


bookId = 1


audiobooklist = query.audioBook(bookId)
soundefectlist = query.soundeffect(bookId)
imageslist = query.image(bookId)
lightlist = query.light(bookId)


# database.create_connection("filename")
audiobook = threading.Thread(target=geluid.sound, args=(audiobooklist,))
soundeffects = threading.Thread(target=geluid.sound, args=(soundefectlist,))
images = threading.Thread(target=beeld.window, args=(imageslist,))
light = threading.Thread(target=verlichting.licht, args=(lightlist,))

audiobook.start()
soundeffects.start()
images.start()
light.start()