import pygame,sys
from random import *
#import math
class MyBall(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left<= screen.get_rect().left or \
                        self.rect.right>= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        if self.rect.top <0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
"""
def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] =-ball.speed[1]
        group.add(ball)
        #ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    #pygame.time.delay(20)
    
"""
pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay,interval)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
image_file = "C:\\Users\\muyicui\\PycharmProjects\\learn-with-kid\\beach_ball.jpg"
#group = pygame.sprite.Group()
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
"""
for row in range(0,3):
    for column in range(0,3):
        location = [column*180+10,row*180+10]
        speed = [choice([-2,2]),choice([-2,2])]
        ball = MyBall(image_file,location,speed)
        group.add(ball)
#y_speed = 5
"""
my_ball = MyBall(image_file,[20,20],[10,0])
pygame.time.set_timer(pygame.USEREVENT,1000)
direction = 1
held = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held = False
        elif event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_UP and my_ball.rect.top > screen.get_rect().top:
                my_ball.rect.top = my_ball.rect.top - 10
            elif event.key == pygame.K_DOWN and my_ball.rect.top < screen.get_rect().bottom - 90:
                my_ball.rect.top = my_ball.rect.top + 10
        elif event.type == pygame.MOUSEMOTION:
            if held:
                my_ball.rect.center = event.pos
        elif event.type == pygame.USEREVENT:
            my_ball.rect.centery = my_ball.rect.centery + 30 * direction
            if my_ball.rect.left <= screen.get_rect().left or \
                my_ball.rect.bottom >= screen.get_rect().bottom:
                direction = -direction
    clock.tick(30)
    screen.blit(background,(0,0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
    #pygame.time.delay(20)
