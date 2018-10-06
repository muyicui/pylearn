import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
plotPoints =[]
colors = []
for x in range(0,640):
    y = int(math.sin(x/640*4*math.pi)*200+240)
    plotPoints.append([x,y])
    colors.append([x,y,x])
    #pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
print(plotPoints)
pygame.draw.lines(screen,colors,False,plotPoints,1)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
