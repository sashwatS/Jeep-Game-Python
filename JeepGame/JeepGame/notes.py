"""
import pygame
pygame.init()

pygame.display.set_caption("killer")
window = pygame.display.set_mode((800, 600))

top_icon = pygame.image.load('gun.png')
pygame.display.set_icon(top_icon)

playerimagexaxis = 100
playerimageyaxis = 100


playerImage = pygame.image.load('5570242431586787256.svg')
def player(x,y):
    window.blit(playerImage,(x,y))

running = True

while running:
    window.fill((255, 0, 0))
    player(20, 425)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

"""