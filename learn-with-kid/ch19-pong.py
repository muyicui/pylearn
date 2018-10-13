import pygame, sys
from random import *


# import math
class MyBall(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global point,score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= screen.get_rect().left or \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            point = point + 1
            score_text = font.render(str(point), 1, (0, 0, 0))

class MyPad(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

image_file = "/Users/muyi/Documents/python/program_with_kids/yellow_ball.jpg"
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])

my_ball = MyBall(image_file, [10, 5], [10, 10])
ballGroup = pygame.sprite.Group(my_ball)
pad = MyPad([270,400])
point = 0
lives = 3
font = pygame.font.Font(None,50)
score_text = font.render(str(point),1,(0,0,0))
textpos = [10,10]
done = False

while True:
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
             pad.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(pad,ballGroup,False):
        my_ball.speed[1] = - my_ball.speed[1]
    my_ball.move()
    if not done:
        screen.blit(my_ball.image, my_ball.rect)
        screen.blit(pad.image,pad.rect)
        screen.blit(score_text,textpos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(my_ball.image,[width-40*i, 20])
        pygame.display.flip()
    if my_ball.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        if lives == 0 :
            final_text1 = "Game Over"
            final_text2 = "Your Final Store is: " + str(point)
            ft1_font = pygame.font.Font(None,70)
            ft2_font = pygame.font.Font(None,50)
            ft1_surf = font.render(final_text1,1,[0,0,0])
            ft2_surf = font.render(final_text2,1,[0,0,0])
            screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2 - ft2_surf.get_width()/2,200])
            pygame.display.flip()

            done = True
            pygame.time.delay(1000)
            pygame.time.delay(1000)
            sys.exit()
        else:
            pygame.time.delay(2000)
            my_ball.rect.topleft = [50,50]