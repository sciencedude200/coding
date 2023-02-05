x = 0
y = 0

x += 9.8 # gravity in x-direction
y += 9.8 # gravity in y-direction

import pygame

pygame.init()

screen = pygame.display.set_mode((1600, 1000))

red_ball = pygame.image.load("red_ball.png")

screen.blit(red_ball, (x, y))

pygame.display.flip()