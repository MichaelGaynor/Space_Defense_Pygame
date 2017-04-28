import pygame
from pygame.sprite import Sprite
from math import hypot

class Projectile(Sprite):
  def __init__(self,screen,turret):
    super(Projectile,self).__init__()
    self.screen = screen
    self.rect = pygame.Rect(0,0,4,4)
    self.rect.centerx = turret[0]
    self.rect.top = turret[1]
    self.color = (255,255,0)
    self.speed = 5
    self.y = self.rect.y
    self.x = self.rect.x

  # def update(self,target):
  #   dx = self.x - target.x
  #   dy = self.y - target.y
  #   dist = hypot(dx,dy)
  #   dx = dx/dist
  #   dy = dy/dist
  #   self.x -= dx * self.speed
  #   self.y -= dy * self.speed
  #   self.rect.left = self.x
  #   self.rect.top = self.y

  # def draw_projectile(self):
  #   pygame.draw.rect(self.screen,self.color,self.rect)


class Missile(Projectile):
  def __init__(self,screen,turret):
    super(Missile,self).__init__(screen,turret)

  def update(self,bogies):
    closest_bogey_dist = 5000
    for target in bogies:
      dx = self.x - target.x
      dy = self.y - target.y
      dist = hypot(dx,dy)
      if dist < closest_bogey_dist:
        closest_bogey_dist = dist
        final_target = target
    dx = self.x - final_target.x
    dy = self.y - final_target.y
    dist = hypot(dx,dy)
    dx = dx/dist
    dy = dy/dist
    self.x -= dx * self.speed
    self.y -= dy * self.speed
    self.rect.left = self.x
    self.rect.top = self.y

  def draw_missile(self):
    pygame.draw.rect(self.screen,self.color,self.rect)


