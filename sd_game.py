# All of our important imports of importance
import pygame
# and from our own files
from player import Player
from home_base import HomeBase
from turret import Turret
from game_functions import check_events
from bogey import Bogey
from pygame.sprite import Group, groupcollide
from random import randint


# --------------------THE CORE GAME FUNCTIONALITY
def run_game():

  pygame.init()
  # --------------------THE SCREEN BASICS
  screen_size = (1000,800)
  background_color = (0,20,0)
  screen = pygame.display.set_mode(screen_size)
  pygame.display.set_caption("SPACE DEFENSE")

  player = Player(screen,"./images/PlayerShip.png",100,100)
  player_group = Group()
  player_group.add(player)
  home_base = HomeBase(screen,"./images/HomeBase.png",100,400)
  home_bases = Group()
  home_bases.add(home_base)
  turret_image = "./images/TurretStation.png"
  turrets = Group()
  bogey = Bogey(screen)
  bogies = Group()
  bogies.add(bogey)
  missiles = Group()

  tick = 0

  while 1:
    tick += 1
    if tick % 10 == 0:
      bogies.add(Bogey(screen))

    screen.fill(background_color)

    check_events(screen,player,turrets,turret_image,missiles)
# drawing enemies, missiles, turrets, and the player
    for player in player_group:
      player.draw_me()

    for home_base in home_bases:
      home_base.draw_me()

    for turret in turrets:
      turret.draw_me()
      turret.open_fire(screen,bogies,missiles,tick)

    for bogey in bogies:
      bogey.draw_me()
      bogey.update_me(home_base)

    for missile in missiles:
      list1 = len(bogies.sprites())
      missile.draw_missile()
      if list1 > 0:
        # target1 = bogies.sprites()[0]
        missile.update(bogies)
      elif list1 <= 0:
        missiles.empty()

# dealing with collisions
    player_died = groupcollide(player_group,bogies,True,False)
    you_lose = groupcollide(home_bases,bogies,True,True)
    missile_hit = groupcollide(missiles,bogies,True,True)

    pygame.display.flip()

run_game()