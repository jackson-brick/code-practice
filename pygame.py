#python3 -m pip install -U pygame==2.6.0
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

