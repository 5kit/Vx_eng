import sys
import os
import math
import random
import time

import pygame

class object():
    def __init__(self, dex, spsz, pos, sc=1, p=False):
        self.p = p
        self.x = pos[0]*unit
        self.y = pos[1]*unit
        self.z = pos[2]*unit
        self.sc = sc
        self.model = (dex, spsz, dex)
        self.dx = 0
        self.dy = 0

    def render3D(self, screen, height, r):
        h = min(2.3,max(0, height))
        x = 75*scale + (self.x+self.dx)*math.cos(r*math.pi/180) + (self.y+self.dy)*math.sin(r*math.pi/180) 
        y = 90*scale - (self.x+self.dx)*math.sin(r*math.pi/180) + (self.y+self.dy)*math.cos(r*math.pi/180) + (1-h*5) + self.z*h/2
        if -5 < x < 155*scale and -5 < y < 165*scale:
            render_stack(display, bk[self.model[0]], self.model[1], (x, y,self.z), r, h, self.sc,self.p or self.model[0]==5)

    def getPriority(self,r):
        value = -1000 * self.z
        value += 90*scale - (self.x+self.dx)*math.sin(r*math.pi/180) + (self.y+self.dy)*math.cos(r*math.pi/180) + (1-h*5) + int(self.z)*h/2
        return value

def render_stack(surf, spritesheet, sprite_size, pos, rotation, spread=1, sc=1, alpha=False):
    sheet_width, sheet_height = spritesheet.get_size()
    sprite_width, sprite_height = sprite_size
    spread *= sc/2
    
    if not alpha:
        spritesheet.convert_alpha()
        spritesheet.set_alpha(max(50,min(255,150 - pos[2]*8)))

    images = []
    for y in range(0, sheet_height, sprite_height):
        rect = pygame.Rect(0, y, sprite_width, sprite_height)
        sprite = spritesheet.subsurface(rect)
        images.append(sprite)

    for i, img in enumerate(images):
        scaled_img = pygame.transform.scale(img, (int(img.get_width() * sc), int(img.get_height() * sc)))
        rotated_img = pygame.transform.rotate(scaled_img, rotation)
        surf.blit(rotated_img, (pos[0] - rotated_img.get_width() // 2, pos[1] - rotated_img.get_height() // 2 - i * spread))

def displayText(screen, text, pos=(5,5), font=None, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, 16) if font == None else font
    info_surface = font.render(text, True, color)
    screen.blit(info_surface, pos)

pygame.init()

scale = 1.5

screen = pygame.display.set_mode((800, 600), 0, 32)
display = pygame.Surface((150*scale, 150*scale))

bk = [pygame.image.load('Models/p.png'), pygame.image.load('Models/bk1.png'), pygame.image.load('Models/bk2.png'), pygame.image.load('Models/bk3.png'), pygame.image.load('Models/tr1.png'), pygame.image.load('Models/rk1.png')]
bk_sz = (8,8)

clock = pygame.time.Clock()
        
r = 45
h = 2
st, et = 0, 0
k = None

map = [
##    [[random.randint(0,4)//4 for _ in range (0,100)] for _ in range(0,100)],
##    [[random.randint(0,4)//4 for _ in range (0,100)] for _ in range(0,100)],
##    ]
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 5, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 5, 0],
        [1, 1, 0, 0, 5, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 5],
        [1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 5, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0, 5],
        [2, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
    ],
    [
        [2, 2, 2, 2, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 2, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 2, 2, 2, 2],
    ],
    [
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3],
    ],
]

strtPos = (7,1,-3)

rz = len(map)//2
rx = strtPos[0]
ry = strtPos[1]

unit = 8 * scale-1

Terrain = []
for nz,mz in enumerate(map):
    for nx, mx in enumerate(mz):
        for ny, my in enumerate(mx):
            if my != 0:
                if my == 4:
                    Terrain.append(object(my, bk_sz, (nx-rx,ny-ry,nz-rz), 3*scale))
                else:
                    Terrain.append(object(my, bk_sz, (nx-rx,ny-ry,nz-rz), scale))

player = object(0, (8,8), (0,0,strtPos[2]), scale, True)
bps = 4

while True:
    dt = et-st
    st = time.time()
    display.fill((0, 0, 0))

    Terrain.sort(key= lambda x: x.getPriority(r))
    dp = True
    fall = True
    for box in Terrain:
        if -unit < box.x+box.dx < unit and -unit < box.y+box.dy < unit and player.z-unit < box.z-1 < player.z+unit:
            if box.model[0] in (1,2,3):
                fall = False
        if dp and player.getPriority(r) < box.getPriority(r):
            player.render3D(screen,h,r*2)
            dp = False
        box.render3D(screen, h,r)
    if dp:
        player.render3D(screen,h,r)
        dp = False
    if fall:
        player.z += 8*unit*dt
    
    if player.z > 10:
        player.z = strtPos[2]*unit
        for b in Terrain:
            b.dx = 0
            b.dy = 0
    
    if k != None:
        if k[pygame.K_RIGHT]:
            r += 60 *dt
        if k[pygame.K_LEFT]:
            r -= 60 *dt
        if k[pygame.K_UP]:
            h -= 2*dt
        if k[pygame.K_DOWN]:
            h += 2*dt
        if k[pygame.K_SPACE]:
            player.z -= 10
        if k[pygame.K_LSHIFT]:
            player.z += 10
        if k[pygame.K_w]:
            flg = False
            for b in Terrain:
                b.dx -= bps*unit*math.sin(r*math.pi/180) *dt
                b.dy += bps*unit*math.cos(r*math.pi/180) *dt
                if -unit < b.x+b.dx < unit and -unit < b.y+b.dy < unit and player.z-unit < b.z < player.z+unit:
                    if b.model[0] in (4,6):
                        flg = True
                    elif b.model[0] in (1,2,3):
                        player.z -= unit
            if flg:
                for b in Terrain:
                    b.dx += bps*unit*math.sin(r*math.pi/180) *dt
                    b.dy -= bps*unit*math.cos(r*math.pi/180) *dt

                        
        if k[pygame.K_s]:
            flg = False
            for b in Terrain:
                b.dx += bps*unit*math.sin(r*math.pi/180) *dt
                b.dy -= bps*unit*math.cos(r*math.pi/180) *dt
                if -unit < b.x+b.dx < unit and -unit < b.y+b.dy < unit and player.z-unit < b.z < player.z+unit:
                    if b.model[0] in (4,6):
                        flg = True
                    elif b.model[0] in (1,2,3):
                        player.z -= unit
            if flg:
                for b in Terrain:
                    b.dx -= bps*unit*math.sin(r*math.pi/180) *dt
                    b.dy += bps*unit*math.cos(r*math.pi/180) *dt

                
        if k[pygame.K_a]:
            flg = False
            for b in Terrain:
                b.dx += bps*unit*math.cos(r*math.pi/180) *dt
                b.dy += bps*unit*math.sin(r*math.pi/180) *dt
                if -unit < b.x+b.dx < unit and -unit < b.y+b.dy < unit and player.z-unit < b.z < player.z+unit:
                    if b.model[0] in (4,6):
                        flg = True
                    elif b.model[0] in (1,2,3):
                        player.z -= unit
            if flg:
                for b in Terrain:
                    b.dx -= bps*unit*math.cos(r*math.pi/180) *dt
                    b.dy -= bps*unit*math.sin(r*math.pi/180) *dt
                
        if k[pygame.K_d]:
            flg = False
            for b in Terrain:
                b.dx -= bps*unit*math.cos(r*math.pi/180) *dt
                b.dy -= bps*unit*math.sin(r*math.pi/180) *dt
                if -unit < b.x+b.dx < unit and -unit < b.y+b.dy < unit and player.z-unit < b.z < player.z+unit:
                    if b.model[0] in (4,6):
                        flg = True
                    elif b.model[0] in (1,2,3):
                        player.z -= unit
            if flg:
                for b in Terrain:
                    b.dx += bps*unit*math.cos(r*math.pi/180) *dt
                    b.dy += bps*unit*math.sin(r*math.pi/180) *dt


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            k = pygame.key.get_pressed()
        if event.type == pygame.KEYUP:
            k = pygame.key.get_pressed()
            
    displayText(display, f"x: {int(Terrain[0].dx)/10}, y: {int(Terrain[0].dy)/10}, z: {int(player.z)/10}")
                
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    et = time.time()
    
