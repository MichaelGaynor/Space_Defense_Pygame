import pygame
from pygame.sprite import Sprite
from projectile import Missile

class Turret(Sprite):
  def __init__(self,screen,player,image):
    super(Turret,self).__init__()
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image,(75,75))
    self.screen = screen
    self.rect = self.image.get_rect()
    # self.rect = (200,200)
    self.rect.centerx = player.rect.centerx
    self.rect.top = player.rect.top
    self.y = player.y
    self.x = player.x


  def draw_me(self):
    self.rect.left = self.x
    self.rect.top = self.y
    self.screen.blit(self.image,[self.x,self.y])

  def open_fire(self,screen,bogies,missiles,tick):
    # my_bulk = pygame.sprite.collide_rect_ratio(10.0)
    baddie_list = pygame.sprite.spritecollide(self,bogies,False,pygame.sprite.collide_rect_ratio(3.0))
    new_missile = Missile(screen,[self.x,self.y])
    if tick % 30 == 0 and baddie_list:
      # new_missile = Missile(screen,[self.x,self.y])
      missiles.add(new_missile)
      # new_missile.update(baddie_list[0])


class AutoTurret(Turret):
  def __init__(self,screen,player,image):
    super(AutoTurret,self).__init__(screen)

  def open_fire(self,screen,bogies,bullets):
    baddie_list = pygame.sprite.spritecollide(self,bogies,False,pygame.sprite.collide_rect_ratio(100.0))
    new_bullet = Bullet(screen,[self.x,self.y])
    if baddie_list:
      bullets.add(new_bullet)