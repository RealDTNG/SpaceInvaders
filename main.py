# Dawson Hoyle, Dylan Baker
# Start: 14/4/2023  End: //
# "Space Invaders" like game

import pygame as py, sys


# Game Setup
py.init()
fps = 60
fpsClock = py.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


#Setup of Starting objects
window = py.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), py.HWSURFACE)
py.display.set_caption("Title")
def display():
    window.fill((255,255,255)) #White background
   
   
while True:
    display()
    for event in py.event.get():
      # if user  QUIT then the screen will close
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
   
    py.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
