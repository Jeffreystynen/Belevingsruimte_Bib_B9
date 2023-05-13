import pygame
import subprocess

# mogelijke oplossing? externe mediaplayer openen op de pi met python met subprocess.
input_file = "/home/dyn/ps1/Belevingsruimte_Bib_B9/Test/music.mp3"
process = subprocess.Popen(['vlc','-b',input_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True) # opent vlc in de achtergrond
process.communicate()  # Wait for VLC to complete playing the audio (optional)

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




