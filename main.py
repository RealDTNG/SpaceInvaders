# Dawson Hoyle, Dylan Baker
# Start: 14/4/2023  End: //
# "Space Invaders" like game

import pygame as pg, sys
from screeninfo import get_monitors # pip install screeninfo


# Game Setup
pg.init()
fps = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500


#Setup of Starting objects
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Title")

def display():
    window.fill((255,255,255)) #White background
    
   
while True:
    display()
    for event in pg.event.get():
      # if user  QUIT then the screen will close 
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
   
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
