import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("C:\\Users\\muyicui\\PycharmProjects\\learn-with-kid\\beach_ball.jpg")
x = 50
y = 50
x_speed = 10
#y_speed = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x = x + x_speed
 #   y = y + y_speed
    if x>screen.get_width()-90:
        x = -90
  #  if y>screen.get_height()-90 or y<0:
   #     y_speed = -y_speed
    screen.blit(my_ball,[x,y])
    pygame.display.flip()

