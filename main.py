# Dawson Hoyle, Dylan Baker
# Start: 14/4/2023  End: //
# "Space Invaders" like game

'''
To do list:

  - exit btn                      > DONE
  - char sprites                  > To Do
  - plan layout/placement         > To Do
    > 900 x 1028 H                < Current Length and Width
  - enemies+movement sequence     > To Do
  - barriers                      > To Do
  - player                        > To Do
  - enemy bullets                 > To Do
  - player bullets                > To Do
  - damage                        > To Do
  - win/lose                      > To Do
  - efx                           > To Do
    > change icon                 < Not Set
  - pause                         > To Do
  - menu                          > To Do
  - keybinds                      > To Do

'''

import pygame as pg, sys
from  button import Button
from screeninfo import get_monitors #pip install screeninfo


# Game Setup
pg.init()
fps = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = int((str(get_monitors()).split(","))[2][7:])
WINDOW_HEIGHT = int((str(get_monitors()).split(","))[3][8:])


def exit():
  pg.quit() 
  sys.exit()


#Setup of Starting objects
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Title")
btn1 = Button(30, 30, 400, 100, 'EXIT ', exit)


def display():
    window.fill((26,26,34)) #Black background
    btn1.process(window)
    

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:# if user  QUIT then the screen will close 
            pg.quit()
            sys.exit()
        key_input = pg.key.get_pressed()
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
