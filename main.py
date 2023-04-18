# Dawson Hoyle, Dylan Baker
# Start: 14/4/2023  End: //
# "Space Invaders" like game

'''
To do list:

  - exit btn (Class)              > DONE
  - char sprites (Class)          > DONE
  - plan layout/placement         > CURRENT
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
from  button_class import Button
from screeninfo import get_monitors #pip install screeninfo
from alian_test import alian


# Game Setup
pg.init()
fps = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = int((str(get_monitors()).split(","))[2][7:])
WINDOW_HEIGHT = int((str(get_monitors()).split(","))[3][8:])


alian_b = pg.image.load('space_invaders_imgs/alian_blue.png')
alian_g = pg.image.load('space_invaders_imgs/alian_green.png')
alian_r = pg.image.load('space_invaders_imgs/alian_red.png')
alian_s = pg.image.load('space_invaders_imgs/alian_ship.png')
alian_p = pg.image.load('space_invaders_imgs/alian_pop.png')
alian_s1 = pg.image.load('space_invaders_imgs/alian_shot_1.png')
alian_s2 = pg.image.load('space_invaders_imgs/alian_shot_2.png')
alian_s3 = pg.image.load('space_invaders_imgs/alian_shot_3.png')


player_s = pg.image.load('space_invaders_imgs/player_ship.png')
player_s1 = pg.image.load('space_invaders_imgs/player_shot.png')


def exit():
  pg.quit() 
  sys.exit()


#Setup of Starting objects
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Title")
btn1 = Button(30, 30, 400, 100, 'EXIT ', exit)


green_group = pg.sprite.Group()
red_group1 = pg.sprite.Group()
red_group2 = pg.sprite.Group()
blue_group1 = pg.sprite.Group()
blue_group2 = pg.sprite.Group()



def alian_green_group():
  global green_list
  green_list = [True,True,True,True,True,True,True,True,True,True]
  green_group.add(alian(500, 200, 44, 32, alian_g))
  green_group.add(alian(550, 200, 44, 32, alian_g))
  green_group.add(alian(600, 200, 44, 32, alian_g))
  green_group.add(alian(650, 200, 44, 32, alian_g))
  green_group.add(alian(700, 200, 44, 32, alian_g))
  green_group.add(alian(750, 200, 44, 32, alian_g))
  green_group.add(alian(800, 200, 44, 32, alian_g))
  green_group.add(alian(850, 200, 44, 32, alian_g))
  green_group.add(alian(900, 200, 44, 32, alian_g))
  green_group.add(alian(950, 200, 44, 32, alian_g))


def alian_red_group1():
  global red_alive_list1,red_g1,red_g2,red_g3,red_g4,red_g5,red_g6,red_g7,red_g8,red_g9,red_g10
  red_alive_list1 = [True,True,True,True,True,True,True,True,True,True]
  red_g1 = alian(500, 240, 44, 32, alian_r)
  red_g2 = alian(550, 240, 44, 32, alian_r)
  red_g3 = alian(600, 240, 44, 32, alian_r)
  red_g4 = alian(650, 240, 44, 32, alian_r)
  red_g5 = alian(700, 240, 44, 32, alian_r)
  red_g6 = alian(750, 240, 44, 32, alian_r)
  red_g7 = alian(800, 240, 44, 32, alian_r)
  red_g8 = alian(850, 240, 44, 32, alian_r)
  red_g9 = alian(900, 240, 44, 32, alian_r)
  red_g10 = alian(950, 240, 44, 32, alian_r)

  red_group1.add(red_g1,red_g2,red_g3,red_g4,red_g5,red_g6,red_g7,red_g8,red_g9,red_g10)


def alian_red_group2():
  global red_list2
  red_list2 = [True,True,True,True,True,True,True,True,True,True]
  red_group2.add(alian(500, 280, 44, 32, alian_r))
  red_group2.add(alian(550, 280, 44, 32, alian_r))
  red_group2.add(alian(600, 280, 44, 32, alian_r))
  red_group2.add(alian(650, 280, 44, 32, alian_r))
  red_group2.add(alian(700, 280, 44, 32, alian_r))
  red_group2.add(alian(750, 280, 44, 32, alian_r))
  red_group2.add(alian(800, 280, 44, 32, alian_r))
  red_group2.add(alian(850, 280, 44, 32, alian_r))
  red_group2.add(alian(900, 280, 44, 32, alian_r))
  red_group2.add(alian(950, 280, 44, 32, alian_r))
def alian_blue_group1():
  global blue_list1
  blue_list1 = [True,True,True,True,True,True,True,True,True,True]
  blue_group1.add(alian(500, 320, 44, 32, alian_b))
  blue_group1.add(alian(550, 320, 44, 32, alian_b))
  blue_group1.add(alian(600, 320, 44, 32, alian_b))
  blue_group1.add(alian(650, 320, 44, 32, alian_b))
  blue_group1.add(alian(700, 320, 44, 32, alian_b))
  blue_group1.add(alian(750, 320, 44, 32, alian_b))
  blue_group1.add(alian(800, 320, 44, 32, alian_b))
  blue_group1.add(alian(850, 320, 44, 32, alian_b))
  blue_group1.add(alian(900, 320, 44, 32, alian_b))
  blue_group1.add(alian(950, 320, 44, 32, alian_b))
def alian_blue_group2():
  global blue_list2
  blue_list2 = [True,True,True,True,True,True,True,True,True,True]
  blue_group2.add(alian(500, 360, 44, 32, alian_b))
  blue_group2.add(alian(550, 360, 44, 32, alian_b))
  blue_group2.add(alian(600, 360, 44, 32, alian_b))
  blue_group2.add(alian(650, 360, 44, 32, alian_b))
  blue_group2.add(alian(700, 360, 44, 32, alian_b))
  blue_group2.add(alian(750, 360, 44, 32, alian_b))
  blue_group2.add(alian(800, 360, 44, 32, alian_b))
  blue_group2.add(alian(850, 360, 44, 32, alian_b))
  blue_group2.add(alian(900, 360, 44, 32, alian_b))
  blue_group2.add(alian(950, 360, 44, 32, alian_b))


alian_green_group()
alian_red_group1()
alian_red_group2()
alian_blue_group1()
alian_blue_group2()




def display():
    window.fill((26,26,34)) #Black background
    btn1.process(window)

    green_group.draw(window)
    red_group1.draw(window)
    red_group2.draw(window)
    blue_group1.draw(window)
    blue_group2.draw(window)
    

while True:
    display()
    for event in pg.event.get():
        if event.type == pg.QUIT:# if user  QUIT then the screen will close 
            pg.quit()
            sys.exit()
        key_input = pg.key.get_pressed()
        pg.sprite.Group(red_group1).update()
        red_g7.alive=False
        
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
