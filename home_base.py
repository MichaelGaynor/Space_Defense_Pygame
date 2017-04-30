import pygame
from pygame.sprite import Sprite

class HomeBase(Sprite):
  def __init__(self,screen,image,start_x,start_y):
    super(HomeBase,self).__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image,(200,200))
    self.x = start_x
    self.y = start_y
    self.screen = screen
    self.rect = self.image.get_rect()


  def draw_me(self):
    self.screen.blit(self.image,[self.x,self.y])