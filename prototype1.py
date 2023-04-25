from pickletools import pyset
import py_compile
from winsound import SND_ALIAS
import pygame
from pygame.locals import *
import random
import math
pygame.init()

def color_algorithm(self_red,self_green,self_blue,red,green,blue):

    if self_red > red:
        self_red -= 1
    if self_red < red:
        self_red += 1
    if self_green < green:
        self_green +=1
    if self_green > green:
        self_green -=1
    if self_blue > blue:
        self_blue -=1
    if self_blue < blue:
        self_blue +=1
    return self_red,self_green,self_blue

def gravity_algorithm(self_x,self_y,x,y):

    if self_x > x:
        self_x -=1
    if self_x < x:
        self_x += 1
    if self_y > y:
        self_y -=1
    if self_y < y:
        self_y +=1
    return [self_x,self_y]


class Snow(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.r = random.randint(1,255)
        self.g = random.randint(1,255)
        self.b = random.randint(1,255)

        self.color = (self.r,self.g,self.b)

        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        self.addieren = random.randint(3,6)
        self.rand_multiply = random.randint(1,3)
        self.sinWert = random.uniform(-math.pi,math.pi)
        
        self.r_fill = [random.randint(1,255) for i in range (3)]

        self.gravity_ = False

        self.ability_to_move = True

    def update(self,color,random_,kill,gravity,gravity_size,move):
        x,y = pygame.mouse.get_pos()
        if kill:
            if self.rect.x + 50 > x > self.rect.x -50 and self.rect.y + 50 > y > self.rect.y - 50:
                self.kill()
        if gravity:
            if self.rect.x + gravity_size > x > self.rect.x -gravity_size and self.rect.y + gravity_size > y > self.rect.y - gravity_size:
                self.gravity_ = True
                self.rect.x,self.rect.y = gravity_algorithm(self.rect.x,self.rect.y,x,y)
                
            else: self.gravity_ = False
        if not gravity:
            self.gravity_ = False
        if not self.gravity_ and move == True and self.ability_to_move == True:        

                self.rect.x += math.sin(self.sinWert) * self.rand_multiply
                self.rect.y += self.addieren
                self.sinWert += 0.1      

        if random_ == True:
            color = self.r_fill
        self.r,self.g,self.b = color_algorithm(self.r,self.g,self.b,int(color[0]),int(color[1]),int(color[2])) 
        self.color = (self.r,self.g,self.b)
        self.image.fill(self.color)
        



        if self.rect.x >= W or self.rect.x < 0:
            self.kill()
        if self.rect.y >= H or self.rect.y < 0:
            self.kill()

W,H = 1920,1080

WIN = pygame.display.set_mode((W,H))

clock = pygame.time.Clock()

fps = 60

sprite_Group = pygame.sprite.Group()

color = [random.randint(1,255) for i in range (3)]

random_ = True

size = 6

kill = False

gravity = False

gravity_size = 100

move = True

spawn = True

shape = False

counter = 0

while True:
    if counter == 1:
        x,y = pygame.mouse.get_pos()
        snow = Snow(size,size,x,y)
        sprite_Group.add(snow)       
    if spawn == True:
        for i in range(4):
            snow = Snow(size,size,random.randint(1,1920),1)
            sprite_Group.add(snow)
        
    
    WIN.fill(("black"))
    for e in pygame.event.get(): 
        if e.type == pygame.QUIT:
            pygame.quit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                random_ = False
                colorSave = color
                color = [random.randint(1,255) for i in range (3)]
                while color == colorSave:
                    color = [random.randint(1,255) for i in range (3)]
            if e.button == 3:
                counter +=1
                if counter ==1:
                    pass
                else:
                    counter = 0



        if e.type == pygame.MOUSEWHEEL:
            gravity_size += e.y * 20

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                random_ = True
            if e.key == pygame.K_l:
                if kill == True:
                    kill = False
                else: kill = True
            if e.key == pygame.K_1:
                size = 1
            if e.key == pygame.K_2:
                size = 2
            if e.key == pygame.K_3:
                size = 3
            if e.key == pygame.K_4:
                size = 4
            if e.key == pygame.K_5:
                size = 5
            if e.key == pygame.K_6:
                size = 6
            if e.key == pygame.K_7:
                size = 7
            if e.key == pygame.K_8:
                size = 8
            if e.key == pygame.K_9:
                size = 9
            if e.key == pygame.K_BACKSPACE:
                sprite_Group.empty()
            if e.key == pygame.K_g:
                if gravity == True:
                    gravity = False
                else:gravity = True  
            if e.key == K_p:
                if move == True:
                    move = False
                else: move = True
            if e.key == K_s:
                if spawn == True:
                    spawn = False
                else: spawn = True
                
    sprite_Group.draw(WIN)

    sprite_Group.update(color,random_,kill,gravity,gravity_size,move)
    
        

    pygame.display.update()
    clock.tick(fps)
