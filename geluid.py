import subprocess
import time

def sound(list):
    if list.count() > 1:
        path = list[0]
    else:
        order = list[0]
        timing = list[1]
        path = list[2]


    for i in range(path.count()):
        input_file = path[i]
        time.sleep(timing[i])
        # start the vlc media player and play the audio file
        subprocess.Popen(['cvlc', input_file])
    






