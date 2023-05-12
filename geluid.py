import pygame 
pygame.init() 

def audiobook(path):
    my_sound = pygame.mixer.Sound(path) 
    my_sound.play() 