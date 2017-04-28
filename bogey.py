import pygame
from pygame.sprite import Sprite
from math import hypot
from random import randint

class Bogey(Sprite):
  def __init__(self,screen):
    super(Bogey,self).__init__()
    self.image = pygame.image.load("./images/EnemyShip.png")
    self.image = pygame.transform.scale(self.image,[20,20])
    self.speed = 2
    self.screen = screen
    self.x = 1000
    self.y = randint(0,800)
    self.rect = self.image.get_rect()

  def update_me(self,player):
    dx = self.x - player.x
    dy = self.y - player.y
    dist = hypot(dx,dy)
    dx = dx/dist
    dy = dy/dist
    self.x -= dx * self.speed
    self.y -= dy * self.speed
    self.rect.left = self.x
    self.rect.top = self.y

  def draw_me(self):
    self.screen.blit(self.image,[self.x,self.y])