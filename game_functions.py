import pygame

import sys
from turret import Turret
from projectile import Missile

def check_events(screen,player,turrets,image,missiles):
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key == 273:
        player.should_move("up", True)
      elif event.key == 274: 
        player.should_move("down", True)
      if event.key == 275:
        player.should_move("right", True)
      elif event.key == 276:
        player.should_move("left", True)
      if event.key == 32:
        new_turret = Turret(screen,player,image)
        turrets.add(new_turret)
      if event.key == 115:
        new_missile = Missile(screen,[player.x,player.y])
        missiles.add(new_missile)

    elif event.type == pygame.KEYUP:
      if event.key == 273:
        player.should_move("up", False)
      elif event.key == 274:
        player.should_move("down", False)
      if event.key == 275:
        player.should_move("right", False)
      elif event.key == 276:
        player.should_move("left", False)