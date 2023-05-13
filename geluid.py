import subprocess
import time

def sound(lijst):
    if len(lijst) < 1:
        print("lijst is leeg")
    elif len(lijst) == 1:
        path = lijst[0]
    else:
        order = lijst[0]
        timing = lijst[1]
        path = lijst[2]


    for i in range(len(path)-1):
        input_file = path[i]
        time.sleep(timing[i])
        # start the vlc media player and play the audio file
        subprocess.Popen(['cvlc', input_file])
    






