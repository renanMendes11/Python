#Reproduzir um audio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load('barco.mp3')
pygame.mixer.music.play()
pygame.event.wait()