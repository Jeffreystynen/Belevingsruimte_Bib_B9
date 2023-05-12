import pathlib 
import os
import pygame

inputdirectory = "/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.wav"

pygame.init()
pygame.mixer.music.load(inputdirectory)

while True:
    n= input("play, pause, stop")
    if n=="play":
        pygame.mixer.music.play()
    elif n=="pause":
        pygame.mixer.music.pause()
    elif n=="exit":
        exit()
