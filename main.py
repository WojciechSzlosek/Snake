import pygame
import sys
from pygame.locals import *

width = 400
height = 300

def death(x,y):
    if(x>width or x<0):
        return 1
    elif(y>height or y<0):
        return -1

    return 0

pygame.init()

timer = pygame.time.Clock()
pygame.display.set_caption('Snake - Wojciech Szlosek')

background_color = (2,55,50)
disp = pygame.display.set_mode((width,height))

pygame.display.update()

x = width/2
y = height/2
x1p = 0
y1p = 0

while True:
    for event in pygame.event.get():


        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                x1p = 0
                y1p = -10
            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                x1p = 0
                y1p = 10
            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                x1p = -10
                y1p = 0
            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                x1p = 10
                y1p = 0


    x+=x1p
    y+=y1p

    disp.fill(background_color)
    pygame.draw.rect(disp,(200,50,100),[x,y,10,10])
    pygame.display.update()

    if(death(x,y)==1):
        if(x<0):
            x = width
        else:
            x = 0
    if(death(x,y)==-1):
        if (y < 0):
            y = height
        else:
            y = 0

    timer.tick(1000000)   # speed of snake

pygame.quit()
quit()