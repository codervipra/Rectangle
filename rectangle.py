import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
done= False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,125),pygame.Rect(100,100,200,100))
    pygame.display.flip()