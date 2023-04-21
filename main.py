# Dawson Hoyle
# Start: 14/4/2023  End: //
# "Space Invaders" like game

'''
To do list:

  - exit btn (Class)              > DONE
  - char sprites (Class)          > DONE
  - plan layout/placement         > 50%
    > 900 x 1028 H                < Current Length and Width
  - enemies+movement sequence     > DONE
  - barriers                      > To Do
  - player                        > 75%
  - enemy bullets                 > To Do
  - player bullets                > 75%
  - damage                        > To Do
  - win/lose                      > To Do
  - efx                           > To Do
    > change icon                 < Not Set
  - pause                         > To Do
  - menu                          > CURRENT TASK
  - keybinds                      > To Do

'''

import pygame as pg, sys
from  button_class import Button
from screeninfo import get_monitors #pip install screeninfo
from alian_test import alian
from player_test import player_
from Bullets import bullet
from pygamevideo import Video


# Game Setup
pg.init()
fps = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = int((str(get_monitors()).split(","))[2][7:])
WINDOW_HEIGHT = int((str(get_monitors()).split(","))[3][8:])
alian_move_type = True
move_alian = False
toggle1_state = False
toggle2_state = True
playing = False
btn_toggle_1_state = '#ffffff'
btn_toggle_2_state = '#ffffff'
vid1 = Video("space_invaders_mp4s/alian1_move.mp4")
vid2 = Video("space_invaders_mp4s/alian2_move.mp4")



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
  
def toggle1():
  global toggle1_state, toggle2_state
  toggle1_state = True
  toggle2_state = False
def toggle2():
  global toggle1_state, toggle2_state
  toggle1_state = False
  toggle2_state = True


#Setup of Starting objects
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.FULLSCREEN)
pg.display.set_caption("Title")
green_group = pg.sprite.Group()
red_group1 = pg.sprite.Group()
red_group2 = pg.sprite.Group()
blue_group1 = pg.sprite.Group()
blue_group2 = pg.sprite.Group()
player_group = pg.sprite.Group()
player_shot_group = pg.sprite.Group()

def player_init():
  global player_state, player
  player_state = True
  
  player = player_(725, 800, 44, 32, player_s)
  player_group.empty()
  player_group.add(player)

def alian_green_group():
  global green_alive_list,green_g1,green_g2,green_g3,green_g4,green_g5,green_g6,green_g7,green_g8,green_g9,green_g10
  green_alive_list = [True,True,True,True,True,True,True,True,True,True]
  
  green_g1 = alian(500, 200, 44, 32, alian_g)
  green_g2 = alian(550, 200, 44, 32, alian_g)
  green_g3 = alian(600, 200, 44, 32, alian_g)
  green_g4 = alian(650, 200, 44, 32, alian_g)
  green_g5 = alian(700, 200, 44, 32, alian_g)
  green_g6 = alian(750, 200, 44, 32, alian_g)
  green_g7 = alian(800, 200, 44, 32, alian_g)
  green_g8 = alian(850, 200, 44, 32, alian_g)
  green_g9 = alian(900, 200, 44, 32, alian_g)
  green_g10 = alian(950, 200, 44, 32, alian_g)
  
  green_group.empty()
  green_group.add(green_g1,green_g2,green_g3,green_g4,green_g5,green_g6,green_g7,green_g8,green_g9,green_g10)

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

  red_group1.empty()
  red_group1.add(red_g1,red_g2,red_g3,red_g4,red_g5,red_g6,red_g7,red_g8,red_g9,red_g10)

def alian_red_group2():
  global red_alive_list2,red_gg1,red_gg2,red_gg3,red_gg4,red_gg5,red_gg6,red_gg7,red_gg8,red_gg9,red_gg10
  red_alive_list2 = [True,True,True,True,True,True,True,True,True,True]
  red_gg1 = alian(500, 280, 44, 32, alian_r)
  red_gg2 = alian(550, 280, 44, 32, alian_r)
  red_gg3 = alian(600, 280, 44, 32, alian_r)
  red_gg4 = alian(650, 280, 44, 32, alian_r)
  red_gg5 = alian(700, 280, 44, 32, alian_r)
  red_gg6 = alian(750, 280, 44, 32, alian_r)
  red_gg7 = alian(800, 280, 44, 32, alian_r)
  red_gg8 = alian(850, 280, 44, 32, alian_r)
  red_gg9 = alian(900, 280, 44, 32, alian_r)
  red_gg10 = alian(950, 280, 44, 32, alian_r)
  
  red_group2.empty()
  red_group2.add(red_gg1,red_gg2,red_gg3,red_gg4,red_gg5,red_gg6,red_gg7,red_gg8,red_gg9,red_gg10)

def alian_blue_group1():
  global blue_alive_list1,blue_g1,blue_g2,blue_g3,blue_g4,blue_g5,blue_g6,blue_g7,blue_g8,blue_g9,blue_g10
  blue_alive_list1 = [True,True,True,True,True,True,True,True,True,True]
  blue_g1 = alian(500, 320, 44, 32, alian_b)
  blue_g2 = alian(550, 320, 44, 32, alian_b)
  blue_g3 = alian(600, 320, 44, 32, alian_b)
  blue_g4 = alian(650, 320, 44, 32, alian_b)
  blue_g5 = alian(700, 320, 44, 32, alian_b)
  blue_g6 = alian(750, 320, 44, 32, alian_b)
  blue_g7 = alian(800, 320, 44, 32, alian_b)
  blue_g8 = alian(850, 320, 44, 32, alian_b)
  blue_g9 = alian(900, 320, 44, 32, alian_b)
  blue_g10 = alian(950, 320, 44, 32, alian_b)
  
  blue_group1.empty()
  blue_group1.add(blue_g1,blue_g2,blue_g3,blue_g4,blue_g5,blue_g6,blue_g7,blue_g8,blue_g9,blue_g10)

def alian_blue_group2():
  global blue_alive_list2,blue_gg1,blue_gg2,blue_gg3,blue_gg4,blue_gg5,blue_gg6,blue_gg7,blue_gg8,blue_gg9,blue_gg10
  blue_alive_list2 = [True,True,True,True,True,True,True,True,True,True]
  
  blue_gg1 = alian(500, 360, 44, 32, alian_b)
  blue_gg2 = alian(550, 360, 44, 32, alian_b)
  blue_gg3 = alian(600, 360, 44, 32, alian_b)
  blue_gg4 = alian(650, 360, 44, 32, alian_b)
  blue_gg5 = alian(700, 360, 44, 32, alian_b)
  blue_gg6 = alian(750, 360, 44, 32, alian_b)
  blue_gg7 = alian(800, 360, 44, 32, alian_b)
  blue_gg8 = alian(850, 360, 44, 32, alian_b)
  blue_gg9 = alian(900, 360, 44, 32, alian_b)
  blue_gg10 = alian(950, 360, 44, 32, alian_b)
  
  blue_group2.empty()
  blue_group2.add(blue_gg1,blue_gg2,blue_gg3,blue_gg4,blue_gg5,blue_gg6,blue_gg7,blue_gg8,blue_gg9,blue_gg10)


def start():
  global playing
  playing = True
  player_init()
  alian_green_group()
  alian_red_group1()
  alian_red_group2()
  alian_blue_group1()
  alian_blue_group2()


btn1 = Button(30, 30, 300, 100, 'EXIT', exit)
btn_toggle_1 = Button(30, 200, 150, 100, f'Alians 1',toggle1)
btn_toggle_2 = Button(180, 200, 150, 100, f'Alians 2', toggle2)
btn_start = Button(30, 300, 300, 100, 'Start', start)
vid1.mute()
vid2.mute()
vid1.set_width(300)
vid2.set_width(300)
vid1.set_height(150)
vid2.set_height(150)


def display():
  global btn_toggle_1_state, btn_toggle_2_state, alian_move_type
  window.fill((26,26,34)) #Black background
  green_group.draw(window)
  red_group1.draw(window)
  red_group2.draw(window)
  blue_group1.draw(window)
  blue_group2.draw(window)
  player_group.draw(window)
  player_shot_group.draw(window)
  
  
  
  if toggle1_state == True:
    btn_toggle_1_state = '#34eb64'
    btn_toggle_2_state = '#e01f36'
    alian_move_type = True
    vid1.play()
    vid2.stop()
  elif toggle2_state == True:
    btn_toggle_2_state = '#34eb64'
    btn_toggle_1_state = '#e01f36'
    alian_move_type = False
    vid1.stop()
    vid2.play()

  
  btn1.process(window)
  btn_start.process(window)
  
  if not playing:
    btn_toggle_1.process(window,btn_toggle_1_state)
    btn_toggle_2.process(window,btn_toggle_2_state)
    if toggle1_state == True and vid1.is_playing == True:
      vid1.draw_to(window, (30, 400))
    elif toggle2_state == True and vid2.is_playing == True:
      vid2.draw_to(window, (30, 400))
  else:
    wall1=pg.draw.rect(window,(235, 247, 247),(1095,0,5,1000))
    wall2=pg.draw.rect(window,(235, 247, 247),(395,0,5,1000))
    
    
    
    
    
def impact(group,alive_group):
  try:
    for each in player_shot_group:
      red_colide= pg.sprite.spritecollide(each, group, False, collided=pg.sprite.collide_mask)  
      if len(red_colide) >0:
        red_colide[0].alive=False
        each.kill()
        alive_group[red_colide[0]] = False
  except: 
    pass
  

def alian_move(first,last):
  global move_alian
  if last.rect.x>1050 or first.rect.x<400:  
    move_alian = True
  else:
    move_alian = False
  display() 
    

shot_time = 0


while True:
    display()
    if playing:
      shot_time += 1
      pg.sprite.Group(green_group).update(alian_move_type, move_alian)
      pg.sprite.Group(red_group1).update(alian_move_type, move_alian)
      pg.sprite.Group(red_group2).update(alian_move_type, move_alian)
      pg.sprite.Group(blue_group1).update(alian_move_type, move_alian)
      pg.sprite.Group(blue_group2).update(alian_move_type, move_alian)
      
      player_shot, player_x = player.move()
      if player_shot == True and shot_time>40:
        shot1 = bullet(player_x+18, 780, 10, 28, player_s1)
        player_shot_group.add(shot1)
        shot_time = 0

      try:
        for each in player_shot_group:
          each.move_play()
          if each.rect.y <0:
            each.kill()
      except:
        pass
      
      impact(green_group, green_alive_list)      
      impact(red_group1, red_alive_list1)
      impact(red_group2, red_alive_list2)
      impact(blue_group1, blue_alive_list1)
      impact(blue_group2, blue_alive_list2)
      
      #if alian_move_type == False:
      alian_move(green_g1,green_g10)
      
      
    for event in pg.event.get():
      if event.type == pg.QUIT:# if user  QUIT then the screen will close 
        exit()
    
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
