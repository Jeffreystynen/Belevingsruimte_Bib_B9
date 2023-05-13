import subprocess
import time

input_file = "/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.mp3"
# start the vlc media player and play the audio file
subprocess.Popen(['cvlc', input_file])
""" 

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Test/music.mp3')

while True:
    n = input("Enter 'play' to start, 'pause' to pause, or 'exit' to quit: ")
    if n == "play":
        pygame.mixer.music.play()
        print("Music started playing")
    elif n == "pause":
        pygame.mixer.music.pause()
        print("Music paused")
    elif n == "exit":
        pygame.mixer.music.stop()
        pygame.quit()
        break
"""




