# All of our important imports of importance
import pygame
# and from our own files
from player import Player
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
  turret_image = "./images/TurretStation.png"
  turrets = Group()
  bogey = Bogey(screen)
  bogies = Group()
  bogies.add(bogey)
  missiles = Group()

  tick = 0

  while 1:
    tick += 1
    if tick % 100 == 0:
      bogies.add(Bogey(screen))

    screen.fill(background_color)

    check_events(screen,player,turrets,turret_image)
# drawing enemies, missiles, turrets, and the player
    for player in player_group:
      player.draw_me()

    for turret in turrets:
      turret.draw_me()
      turret.open_fire(screen,bogies,missiles,tick)

    for bogey in bogies:
      bogey.draw_me()
      bogey.update_me(player)

    for missile in missiles:
      list1 = len(bogies.sprites())
      missile.draw_missile()
      if list1 > 0:
        target1 = bogies.sprites()[0]
        missile.update(target1)
      elif list1 <= 0:
        missiles.empty()

# dealing with collisions
    player_died = groupcollide(player_group,bogies,True,False)
    # turret_died = groupcollide(turrets,bogies,True,True)
    missile_hit = groupcollide(missiles,bogies,True,True)

    pygame.display.flip()

run_game()