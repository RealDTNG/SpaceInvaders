# Dawson Hoyle, Dylan Baker
# Start: 14/4/2023  End: //
# "Space Invaders" like game

'''
To do list:

  - exit btn
  - char sprites
  - plan layout/placement
    > 900 x 1028 H
  - enemies+movement sequence
  - barriers
  - player
  - enemy bullets
  - player bullets
  - damage
  - win/lose
  - efx
    > change icon
  - pause
  - menu
  - keybinds

'''

import pygame as pg, sys, button as btn
from screeninfo import get_monitors #pip install screeninfo


# Game Setup
pg.init()
fps = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = int((str(get_monitors()).split(","))[2][7:])
WINDOW_HEIGHT = int((str(get_monitors()).split(","))[3][8:])


#Setup of Starting objects
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Title")


def display():
    window.fill((26,26,34)) #Black background


def exit():
  pg.quit() 
  sys.exit()

btn(30, 30, 400, 100, 'Button One (onePress)', exit )      

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:# if user  QUIT then the screen will close 
            pg.quit()
            sys.exit()
        key_input = pg.key.get_pressed()
        if key_input[pg.K_q]:
            pg.quit()
            sys.exit()
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
