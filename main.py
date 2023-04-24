from pickletools import pyset
import py_compile
from winsound import SND_ALIAS
import pygame
from pygame.locals import *
import random
import math
pygame.init()

def algorithm(self_red,self_green,self_blue,red,green,blue):
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


        self.addieren = random.randint(1,3)
        self.rand_multiply = random.randint(1,3)
        self.sinWert = random.uniform(-math.pi,math.pi)
        
        self.r_fill = [random.randint(1,255) for i in range (3)]

    def update(self,color,random_):

        if random_ == True:
            color = self.r_fill
        self.r,self.g,self.b = algorithm(self.r,self.g,self.b,int(color[0]),int(color[1]),int(color[2])) 
        self.color = (self.r,self.g,self.b)
        self.image.fill(self.color)
        


        self.rect.x += math.sin(self.sinWert) * self.rand_multiply
        self.rect.y += self.addieren
        self.sinWert += 0.1
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

while True:
    for i in range(4):
        snow = Snow(2,2,random.randint(1,1920),1)
        sprite_Group.add(snow)
        
    
    WIN.fill(("black"))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            random_ = False
            colorSave = color
            color = [random.randint(1,255) for i in range (3)]
            while color == colorSave:
                color = [random.randint(1,255) for i in range (3)]
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                random_ = True
            
            
    sprite_Group.draw(WIN)

    sprite_Group.update(color,random_)
    
        

    pygame.display.update()
    clock.tick(fps)
