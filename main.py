import database
import geluid
import beeld
import threading
import verlichting



# database.create_connection("filename")
audiobook = threading.Thread(target=geluid.sound args=)
soundeffects = threading.Thread(target=geluid.sound args=)
images = threading.Thread(target=beeld.window args=)
light = threading.Thread(target=verlichting.licht args=)

audiobook.start()
soundeffects.start()
images.start()
light.start()