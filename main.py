import pygame
import sys
import random
from pygame.locals import *

width = 400
height = 300
block_size = 10

def randomsDivide(x):

    n = 1
    while n%block_size!=0:
        n = random.randint(1,x-1)

    return n

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
eat_color = (255,100,105)

disp = pygame.display.set_mode((width,height))
pygame.display.update()

snake = []
snake_length = 1

x = width/2
y = height/2
x1p = 0
y1p = 0
x_eat = randomsDivide(width)
y_eat = randomsDivide(height)

score = 0

while True:

    for event in pygame.event.get():

        if event.type==QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                x1p = 0
                y1p = -block_size
            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                x1p = 0
                y1p = block_size
            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                x1p = -block_size
                y1p = 0
            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                x1p = block_size
                y1p = 0

    x+=x1p
    y+=y1p

    head = [x,y]
    snake.append(head)

    disp.fill(background_color)

    if(len(snake)>snake_length):
        del snake[0]

    for f in snake:
        pygame.draw.rect(disp,(200,50,100),[f[0],f[1],block_size,block_size])

    pygame.draw.rect(disp,eat_color,[x_eat,y_eat,block_size,block_size])
    pygame.display.update()

    for f in snake[:-1]:
        if f==head:
            print("YOUR SCORE: " + str(score))
            sys.exit()

    if(x==x_eat and y==y_eat):
        x_eat = randomsDivide(width)
        y_eat = randomsDivide(height)
        snake_length+=1
        score+=1

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

    timer.tick(10)   # speed of snake

pygame.quit()
quit()