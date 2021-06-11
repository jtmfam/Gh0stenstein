import pygame
from pygame.locals import *
import math
import worldManager
import time

worldMap =[
  [8,8,8,8,8,8,8,8,8,8,8,4,4,6,4,4,6,4,6,4,4,4,6,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
  [8,0,3,3,0,0,0,0,0,8,8,4,0,0,0,0,0,0,0,0,0,0,0,4],
  [8,0,0,0,0,0,0,0,0,0,8,4,0,0,0,0,0,6,6,6,0,6,4,6],
  [8,8,8,8,0,8,8,8,8,8,8,4,4,4,4,4,4,6,0,0,0,0,0,6],
  [7,7,7,7,0,7,7,7,7,0,8,0,8,0,8,0,8,4,0,4,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,0,0,0,0,0,6],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,0,0,0,0,4],
  [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,6,0,6,0,6,0,6],
  [7,7,0,0,0,0,0,0,7,8,0,8,0,8,0,8,8,6,4,6,0,6,6,6],
  [7,7,7,7,0,7,7,7,7,8,8,4,0,6,8,4,8,3,3,3,0,3,3,3],
  [2,2,2,2,0,2,2,2,2,4,6,4,0,0,6,0,6,3,0,0,0,0,0,3],
  [2,2,0,0,0,0,0,2,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [2,0,0,0,0,0,0,0,2,4,0,0,0,0,0,0,4,3,0,0,0,0,0,3],
  [1,0,0,0,0,0,0,0,1,4,4,4,4,4,6,0,6,3,3,0,0,0,3,3],
  [2,0,0,0,0,0,0,0,2,2,2,1,2,2,2,6,6,0,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
  [2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,5,0,5,0,5,0,5,0,5],
  [2,2,0,0,0,0,0,2,2,2,0,0,0,2,2,0,5,0,5,0,0,0,5,5],
  [2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,5,5,5,5,5,5,5,5,5]
];

#worldMap =[
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
#  [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#];

def load_image(image, darken, colorKey = None):
    ret = []
    if colorKey is not None:
        image.set_colorkey(colorKey)
    if darken:
        image.set_alpha(127)
    for i in range(image.get_width()):
        s = pygame.Surface((1, image.get_height())).convert()
        #s.fill((0,0,0))
        s.blit(image, (- i, 0))
        if colorKey is not None:
            s.set_colorkey(colorKey)
        ret.append(s)
    return ret

def main():
  
    t = time.clock() #time of current frame
    oldTime = 0. #time of previous frame
    pygame.mixer.init()
    #pygame.mixer.music.load("MuseUprising.mp3")
    #pygame.mixer.music.play(-1)
    pinky_bite = pygame.mixer.Sound("pinky_bite.ogg")
    size = w, h = 640,480
    pygame.init()
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Gh0stenstein")
    screen = pygame.display.get_surface()
    #pixScreen = pygame.surfarray.pixels2d(screen)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    
    f = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    
    wm = worldManager.WorldManager(worldMap, 22, 11.5, -1, 0, 0, .66)
    
    weapons = [Weapon("fist"),
               Weapon("pistol"),
               Weapon("shotgun"),
               Weapon("dbshotgun"),
               Weapon("chaingun"),
               Weapon("plasma"),
               Weapon("rocket"),
               Weapon("bfg"),
               Weapon("chainsaw")
               ]
    weapon_numbers = [K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_0]
    weapon = weapons[0]
    sprite_positions=[
      (20.5, 11.5, 2, 0,  0., 0.,  0), #green light in front of playerstart
      #green lights in every room
      (18.5,  4.5, 2, 0,  0., 0.,  0),
      (10.0,  4.5, 2, 0,  0., 0.,  0),
      (10.0, 12.5, 2, 0,  0., 0.,  0),
      (3.5,   6.5, 2, 0,  0., 0.,  0),
      (3.5,  20.5, 2, 0,  0., 0.,  0),
      (3.5,  14.5, 2, 0,  0., 0.,  0),
      (14.5, 20.5, 2, 0,  0., 0.,  0),
      
      #row of pillars in front of wall: fisheye test
      (18.5, 10.5, 1, 0,  0., 0.,  0),
      (18.5, 11.5, 1, 0,  0., 0.,  0),
      (18.5, 12.5, 1, 0,  0., 0.,  0)
    ]

    pinkies = [
      #some pinky around the map
      #   x,   y, image#, right_left_foot, start_x, start_y, distance_to_player
      # right_left_foot, zero means leftfoot image, one means right foot image
      # When distance of (start_x, start_y) from (x,y) is more than 6, then change feet
      # If distance_to_player<6, then advance to the player
      Pinky(21.5,  1.5, 3, 0,  21.5,  1.5,  0),
      Pinky(15.5,  1.5, 3, 0,  15.5,  1.5,  0),
      Pinky(16.0,  1.8, 3, 0,  16.0,  1.8,  0),
      Pinky(16.2,  1.2, 3, 0,  16.2,  1.2,  0),
      Pinky(3.5,   2.5, 3, 0,   3.5,  2.5,  0),
      Pinky(9.5,  15.5, 3, 0,   9.5, 15.5,  0),
      Pinky(10.0, 15.1, 3, 0,  10.0, 15.1,  0),
      Pinky(10.5, 15.8, 3, 0,  10.5, 15.8,  0)
    ]

    
    foot=0
    foot_time=0.0
    while(True):
        clock.tick(60)
        
        wm.draw(screen, sprite_positions + [(q.x, q.y, q.pngNum, q.right_left_foot, q.start_x, q.start_y, q.distance_to_player) for q in pinkies] )
        
        
        # timing for input and FPS counter
        
        frameTime = float(clock.get_time()) / 1000.0 # frameTime is the time this frame has taken, in seconds
        t = time.clock()
        #text = f.render(str(foot_time), False, (255, 255, 0))
        text = f.render(str(clock.get_fps()), False, (255, 255, 0))
        screen.blit(text, text.get_rect(), text.get_rect())
        weapon.draw(screen, t)

        # speed modifiers
        moveSpeed = frameTime * 6.0 # the constant value is in squares / second
        rotSpeed = frameTime * 2.0 # the constant value is in radians / second
        pinkySpeed = frameTime * 4.0 # the constant value is in squares / second

        for p in pinkies:
           p.attack(t, wm, pinkySpeed, pinky_bite)
           #DEBUG print p.right_left_foot
        #DEBUG print
        pygame.display.flip()

        for event in pygame.event.get(): 
            if event.type == QUIT: 
                return 
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                elif event.key == K_SPACE:
                    #shoot
                    weapon.play()
                elif event.key in weapon_numbers:
                    weapon.stop()
                    weapon = weapons[weapon_numbers.index(event.key)]
            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    weapon.stop()
            else:
                pass 
        
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            # move forward if no wall in front of you
            moveX = wm.camera.x + wm.camera.dirx * moveSpeed
            if(worldMap[int(moveX)][int(wm.camera.y)]==0 and worldMap[int(moveX + 0.1)][int(wm.camera.y)]==0):wm.camera.x += wm.camera.dirx * moveSpeed
            moveY = wm.camera.y + wm.camera.diry * moveSpeed
            if(worldMap[int(wm.camera.x)][int(moveY)]==0 and worldMap[int(wm.camera.x)][int(moveY + 0.1)]==0):wm.camera.y += wm.camera.diry * moveSpeed
        if keys[K_DOWN]:
            # move backwards if no wall behind you
            if(worldMap[int(wm.camera.x - wm.camera.dirx * moveSpeed)][int(wm.camera.y)] == 0):wm.camera.x -= wm.camera.dirx * moveSpeed
            if(worldMap[int(wm.camera.x)][int(wm.camera.y - wm.camera.diry * moveSpeed)] == 0):wm.camera.y -= wm.camera.diry * moveSpeed
        if (keys[K_RIGHT] and not keys[K_DOWN]) or (keys[K_LEFT] and keys[K_DOWN]):
            # rotate to the right
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(- rotSpeed) - wm.camera.diry * math.sin(- rotSpeed)
            wm.camera.diry = oldDirX * math.sin(- rotSpeed) + wm.camera.diry * math.cos(- rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(- rotSpeed) - wm.camera.planey * math.sin(- rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(- rotSpeed) + wm.camera.planey * math.cos(- rotSpeed)
        if (keys[K_LEFT] and not keys[K_DOWN]) or (keys[K_RIGHT] and keys[K_DOWN]): 
            # rotate to the left
            # both camera direction and camera plane must be rotated
            oldDirX = wm.camera.dirx
            wm.camera.dirx = wm.camera.dirx * math.cos(rotSpeed) - wm.camera.diry * math.sin(rotSpeed)
            wm.camera.diry = oldDirX * math.sin(rotSpeed) + wm.camera.diry * math.cos(rotSpeed)
            oldPlaneX = wm.camera.planex
            wm.camera.planex = wm.camera.planex * math.cos(rotSpeed) - wm.camera.planey * math.sin(rotSpeed)
            wm.camera.planey = oldPlaneX * math.sin(rotSpeed) + wm.camera.planey * math.cos(rotSpeed)

fps = 8
class Weapon(object):
    
    def __init__(self, weaponName="shotgun", frameCount = 5):
        self.images = []
        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0
        for i in range(frameCount):
            img = pygame.image.load("pics/weapons/%s%s.bmp" % (weaponName, i+1)).convert()
            img = pygame.transform.scale2x(img)
            img = pygame.transform.scale2x(img)
            img.set_colorkey(img.get_at((0,0)))
            self.images.append(img)
    def play(self):
        self.playing = True
        self.loop = True
    def stop(self):
        self.playing = False
        self.loop = False
    def draw(self, surface, time):
        if(self.playing or self.frame > 0):
            if(time > self.oldTime + 1./fps):
                self.frame = (self.frame+1) % len(self.images)
                if self.frame == 0: 
                    if self.loop:
                        self.frame = 1
                    else:
                        self.playing = False
                        
                self.oldTime = time
        img = self.images[self.frame]
        surface.blit(img, (surface.get_width()/2 - img.get_width()/2, surface.get_height()-img.get_height()))

mad_threashold = 5
class Pinky(object):
    def __init__(self, x,   y, pngNum, right_left_foot, start_x, start_y, distance_to_player):
        self.x = x
        self.y = y
        self.pngNum = pngNum
        self.right_left_foot = right_left_foot
        self.start_x = x
        self.start_y = y
        self.distance_to_player = distance_to_player

        self.mad = 0

        self.loop = False
        self.playing = False
        self.frame = 0
        self.oldTime = 0

    #def play(self):
    #    self.playing = True
    #    self.loop = True
    #def stop(self):
    #    self.playing = False
    #    self.loop = False
    def attack(self, time, wm, pinkySpeed, pinky_bite):
        #if(self.playing or self.frame > 0):
        #if(time > self.oldTime + 1./fps):
        dx = wm.camera.x - self.x
        dy = wm.camera.y - self.y
        self.distance_to_player = math.sqrt(dx*dx + dy*dy)
        self.mad = 0 # HACK, this is the be able to get away from a pinky
        if self.mad == 0:
           if self.distance_to_player < mad_threashold:
              self.mad = 1
        if (self.mad == 1):
           if self.distance_to_player > 1:
              moveX = self.x + pinkySpeed * dx / self.distance_to_player
              moveY = self.y + pinkySpeed * dy / self.distance_to_player
              if(worldMap[int(moveX)][int(self.y)]==0 and worldMap[int(moveX + 0.1)][int(self.y)]==0):self.x = moveX
              if(worldMap[int(self.x)][int(moveY)]==0 and worldMap[int(self.x)][int(moveY + 0.1)]==0):self.y = moveY
              if (time > self.oldTime + 1.):
                 pinky_bite.play()
                 self.right_left_foot = (self.right_left_foot + 1) % 2
                 self.oldTime = time

if __name__ == '__main__':
    main()
