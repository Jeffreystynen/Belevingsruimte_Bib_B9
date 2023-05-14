import geluid
import beeld
import threading
import verlichting
import query
import time
import psutil

def kill_processes(process_name):
    for proc in psutil.process_iter():
        try:
            if proc.name() == process_name:
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

audiobooklist = []
soundefectlist = []
imageslist = []
lightlist = []

def getready(bookId):
    global audiobooklist, soundefectlist, lightlist, imageslist, light, images, soundeffects, audiobook, lock
    audiobooklist = query.audioBook(bookId)
    soundefectlist = query.soundeffect(bookId)
    imageslist = query.image(bookId)
    lightlist = query.light(bookId)
        
    # database.create_connection("filename")
    audiobook = threading.Thread(target=geluid.book, args=(audiobooklist,))
    soundeffects = threading.Thread(target=geluid.sound, args=(soundefectlist,))
    images = threading.Thread(target=beeld.window, args=(imageslist,))
    light = threading.Thread(target=verlichting.licht, args=(lightlist,))
    


def start():
    global light, images, soundeffects, audiobook, lock
    light.start()
    audiobook.start()
    soundeffects.start()
    images.start()


def done():
    kill_processes('th')
    kill_processes('tk')
    kill_processes('vlc')
