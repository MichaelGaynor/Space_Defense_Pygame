# All of our important imports of importance
import pygame
# and from our own files
from player import Player
from home_base import HomeBase
from turret import AutoTurret
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
  auto_turret_image = "./images/AutoTurret.png"
  auto_turrets = Group()
  bogey = Bogey(screen)
  bogies = Group()
  bogies.add(bogey)
  missiles = Group()
  bullets = Group()

  tick = 0

  pygame.mixer.music.load("sounds/bensound-funkyelement.wav")
  pygame.mixer.music.play(-1)



  while 1:
    tick += 1
    if tick % 10 == 0:
      bogies.add(Bogey(screen))

    screen.fill(background_color)

    check_events(screen,player,turrets,turret_image,missiles,auto_turrets,auto_turret_image,bullets)
# drawing enemies, missiles, turrets, and the player

    for home_base in home_bases:
      home_base.draw_me()

    for player in player_group:
      player.draw_me()

    for auto_turret in auto_turrets:
      auto_turret.draw_me()
      auto_turret.open_fire(screen,bogies,bullets,tick)

    for turret in turrets:
      turret.draw_me()
      turret.open_fire(screen,bogies,missiles,tick)

    for bogey in bogies:
      bogey.draw_me()
      bogey.update_me(home_base,home_bases)
      if bogey.update_me(home_base,home_bases) <= 5:
        bogies.remove(bogey)

    for missile in missiles:
      list1 = len(bogies.sprites())
      missile.draw_missile()
      if list1 > 0:
        # target1 = bogies.sprites()[0]
        missile.update(bogies)
      elif list1 <= 0:
        missiles.empty()

    for bullet in bullets:
      bullet.draw_bullet()
      bullet.update(bogies)

# dealing with collisions
    font = pygame.font.Font(None, 50)
    if len(home_bases.sprites()) != 1:
      loss_text = font.render("You lose. Earth has fallen. Good job. Some hero you are.", True, (255,0,255))
      screen.blit(loss_text, [40,40])


    player_died = groupcollide(player_group,bogies,True,False)
    you_lose = groupcollide(home_bases,bogies,True,False)
    missile_hit = groupcollide(missiles,bogies,True,True)
    bullet_hit = groupcollide(bullets,bogies,True,True)
    turret_hit = groupcollide(turrets,bogies,True,True)
    auto_turret_hit = groupcollide(auto_turrets,bogies,True,True)

    pygame.display.flip()

run_game()