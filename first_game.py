#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:04:11 2021

@author: teresaferreira
"""

import pygame
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Platformer")

#define game variables
tile_size = 100

#load images
sky_image=pygame.image.load('/Users/teresaferreira/Desktop/images_game/sky.jpg')

def draw_grid():
    for line in range(0,6):
        pygame.draw.line(screen,(255,255,255), (0, line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen,(255,255,255), (line*tile_size,0), (line*tile_size,screen_height))

class World():
    def __init__(self,data):
        self.tile_list=[]
        #upload image
        dirt_img=pygame.image.load('/Users/teresaferreira/Desktop/images_game/dirt.png')
        
        row_count=0
        for row in data:
            col_count=0
            for tile in row:
                if tile==1:
                    img = pygame.transform.scale(dirt_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile=(img,img_rect)
                    self.tile_list.append(tile)
                col_count+=1
            row_count+=1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
        
world_data=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,1,1],
    [0,0,0,1,1,1],
    [1,1,1,1,1,1]
    ]
  
world=World(world_data)  

run=True
while run==True:
    screen.blit(sky_image,(0,0))
    
    world.draw()
    draw_grid()
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    pygame.display.update()
            
pygame.quit()