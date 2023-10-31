import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((450,400))
pygame.display.set_caption("Draw")
pygame.display.flip()
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit("Safely exited")
    if event.type == pygame.MOUSEBUTTONDOWN:
        print('Position: ', event.pos)
        mx, my = event.pos
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pygame.draw.circle(screen, (r, g, b,), (mx, my), 10)
        pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        pass
    if event.type == pygame.MOUSEMOTION:
        pass
    
