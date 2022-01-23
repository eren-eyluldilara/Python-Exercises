import random
import pygame

pygame.init()

WHITE=[255,255,255]
BLACK=[0,0,0]
SIZE=[800,400]

screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snowing")

snowFall=[]
for i in range(50):
    x=random.randrange(0,800)
    y=random.randrange(0,400)
    snowFall.append([x,y])

clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            break
    screen.fill(BLACK)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen,WHITE,snowFall[i],2)


        snowFall[i][1] +=1
        if snowFall[i][1] > 400 :
            y=random.randrange(-50,-10)
            snowFall[i][1]=y

            x=random.randrange(0,800)
            snowFall[i][0]=x
    pygame.display.flip()
    clock.tick(20)
pygame.quit()