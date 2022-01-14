# Reproduzir arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('exemplo.mp3')
pygame.mixer.music.play()
pygame.fastevent.wait()