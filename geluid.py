import pygame

input_file = "/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.mp3"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(input_file)

while True:
    n = input("Enter 'play' to start, 'pause' to pause, or 'exit' to quit: ")
    if n == "play":
        pygame.mixer.music.play()
    elif n == "pause":
        pygame.mixer.music.pause()
    elif n == "exit":
        pygame.mixer.music.stop()
        break

pygame.quit()
