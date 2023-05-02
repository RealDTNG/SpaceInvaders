# Dawson Hoyle
# Start: 14/4/2023  End: //
# "Space Invaders" like game

'''
To do list:

  - exit btn (Class)              > DONE
  - char sprites (Class)          > DONE
  - plan layout/placement         > DONE
    > 900 x 1028 H                < Current Length and Width
  - enemies+movement sequence     > DONE
  - barriers                      > DONE
  - player                        > DONE
  - enemy bullets                 > DONE
  - player bullets                > DONE
  - damage                        > DONE
  - win/lose                      > 50%

'''

import pygame as pg, sys, random
from  button_class import Button
from screeninfo import get_monitors #pip install screeninfo
from alian_test import alian
from player_test import player_
from Bullets import bullet
from bariars import bar 
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
vid2 = Video("space_invaders_mp4s/alian1_move.mp4")
vid1 = Video("space_invaders_mp4s/alian2_move.mp4")
pg.font.init()
my_font = pg.font.Font('slkscr.ttf', 40)
playing_pause = False
player_life = 3
score = 0
ending = False
winning = False


alian_b = pg.image.load('space_invaders_imgs/alian_blue.png')
alian_g = pg.image.load('space_invaders_imgs/alian_green.png')
alian_r = pg.image.load('space_invaders_imgs/alian_red.png')
alian_s = pg.image.load('space_invaders_imgs/alian_ship.png')
alian_p = pg.image.load('space_invaders_imgs/alian_pop.png')
alian_s1 = pg.image.load('space_invaders_imgs/alian_shot_1.png')
alian_s3 = pg.image.load('space_invaders_imgs/alian_shot_3.png')

player_s = pg.image.load('space_invaders_imgs/player_ship.png')
player_s1 = pg.image.load('space_invaders_imgs/player_shot.png')

top_center = pg.image.load('space_invaders_imgs/top_center.png')
top_right = pg.image.load('space_invaders_imgs/top_right.png')
top_left = pg.image.load('space_invaders_imgs/top_left.png')
middle_center = pg.image.load('space_invaders_imgs/middle_center.png')
middle_right = pg.image.load('space_invaders_imgs/middle_right.png')
middle_left = pg.image.load('space_invaders_imgs/middle_left.png')
middle2_center = pg.image.load('space_invaders_imgs/middle2_center.png')
middle2_right = pg.image.load('space_invaders_imgs/middle2_right.png')
middle2_left = pg.image.load('space_invaders_imgs/middle2_left.png')
bottom_center = pg.image.load('space_invaders_imgs/bottom_center.png')
bottom_right = pg.image.load('space_invaders_imgs/bottom_right.png')
bottom_left = pg.image.load('space_invaders_imgs/bottom_left.png')


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
bar_group1 = pg.sprite.Group()
bar_group2 = pg.sprite.Group()
bar_group3 = pg.sprite.Group()
player_group = pg.sprite.Group()
player_shot_group = pg.sprite.Group()
player_life_group = pg.sprite.Group()
alian_shot_group = pg.sprite.Group()

def player_init():
  global player
  
  player = player_(725, 800, 44, 32, player_s)
  player_group.empty()
  player_group.add(player)
  
def player_life_check():
  global player_life, player_life_sprite1,player_life_sprite2
  player_life_group.empty()
  
  if player_life == 3:
    player_life_sprite1 = player_(30, 800, 44, 32, player_s)
    player_life_sprite2 = player_(80, 800, 44, 32, player_s)
    player_life_group.add(player_life_sprite1,player_life_sprite2)
  if player_life == 2:
    player_life_sprite1 = player_(30, 800, 44, 32, player_s)
    player_life_group.add(player_life_sprite1)
  if player_life <= 1:
    pass
  
def bar_group1_init():
  
  bar1 = bar(663,670,176,96,top_center)
  bar2 = bar(663,670,176,96,top_right)
  bar3 = bar(663,670,176,96,top_left)
  bar4 = bar(663,670,176,96,middle_center)
  bar5 = bar(663,670,176,96,middle_left)
  bar6 = bar(663,670,176,96,middle_right)
  bar7 = bar(663,670,176,96,middle2_center)
  bar8 = bar(663,670,176,96,middle2_left)
  bar9 = bar(663,670,176,96,middle2_right)
  bar10 = bar(663,670,176,96,bottom_center)
  bar11 = bar(663,670,176,96,bottom_left)
  bar12 = bar(663,670,176,96,bottom_right)
  
  bar_group1.add(bar1,bar2,bar3,bar4,bar5,bar6,bar7,bar8,bar9, bar10, bar11, bar12)
  
def bar_group2_init():
  
  bar1 = bar(463,670,176,96,top_center)
  bar2 = bar(463,670,176,96,top_right)
  bar3 = bar(463,670,176,96,top_left)
  bar4 = bar(463,670,176,96,middle_center)
  bar5 = bar(463,670,176,96,middle_left)
  bar6 = bar(463,670,176,96,middle_right)
  bar7 = bar(463,670,176,96,middle2_center)
  bar8 = bar(463,670,176,96,middle2_left)
  bar9 = bar(463,670,176,96,middle2_right)
  bar10 = bar(463,670,176,96,bottom_center)
  bar11 = bar(463,670,176,96,bottom_left)
  bar12 = bar(463,670,176,96,bottom_right)
  
  bar_group2.add(bar1,bar2,bar3,bar4,bar5,bar6,bar7,bar8,bar9, bar10, bar11, bar12)
  
def bar_group3_init():
  
  bar1 = bar(863,670,176,96,top_center)
  bar2 = bar(863,670,176,96,top_right)
  bar3 = bar(863,670,176,96,top_left)
  bar4 = bar(863,670,176,96,middle_center)
  bar5 = bar(863,670,176,96,middle_left)
  bar6 = bar(863,670,176,96,middle_right)
  bar7 = bar(863,670,176,96,middle2_center)
  bar8 = bar(863,670,176,96,middle2_left)
  bar9 = bar(863,670,176,96,middle2_right)
  bar10 = bar(863,670,176,96,bottom_center)
  bar11 = bar(863,670,176,96,bottom_left)
  bar12 = bar(863,670,176,96,bottom_right)
  
  bar_group3.add(bar1,bar2,bar3,bar4,bar5,bar6,bar7,bar8,bar9, bar10, bar11, bar12)

def alian_green_group():
  global green_g1,green_g2,green_g3,green_g4,green_g5,green_g6,green_g7,green_g8,green_g9,green_g10

  
  green_g1 = alian(500, 200, 44, 32, alian_g,250)
  green_g2 = alian(550, 200, 44, 32, alian_g,250)
  green_g3 = alian(600, 200, 44, 32, alian_g,250)
  green_g4 = alian(650, 200, 44, 32, alian_g,250)
  green_g5 = alian(700, 200, 44, 32, alian_g,250)
  green_g6 = alian(750, 200, 44, 32, alian_g,250)
  green_g7 = alian(800, 200, 44, 32, alian_g,250)
  green_g8 = alian(850, 200, 44, 32, alian_g,250)
  green_g9 = alian(900, 200, 44, 32, alian_g,250)
  green_g10 = alian(950, 200, 44, 32, alian_g,250)
  
  green_group.empty()
  green_group.add(green_g1,green_g2,green_g3,green_g4,green_g5,green_g6,green_g7,green_g8,green_g9,green_g10)

def alian_red_group1():
  global red_g1,red_g2,red_g3,red_g4,red_g5,red_g6,red_g7,red_g8,red_g9,red_g10

  red_g1 = alian(500, 240, 44, 32, alian_r,150)
  red_g2 = alian(550, 240, 44, 32, alian_r,150)
  red_g3 = alian(600, 240, 44, 32, alian_r,150)
  red_g4 = alian(650, 240, 44, 32, alian_r,150)
  red_g5 = alian(700, 240, 44, 32, alian_r,150)
  red_g6 = alian(750, 240, 44, 32, alian_r,150)
  red_g7 = alian(800, 240, 44, 32, alian_r,150)
  red_g8 = alian(850, 240, 44, 32, alian_r,150)
  red_g9 = alian(900, 240, 44, 32, alian_r,150)
  red_g10 = alian(950, 240, 44, 32, alian_r,150)

  red_group1.empty()
  red_group1.add(red_g1,red_g2,red_g3,red_g4,red_g5,red_g6,red_g7,red_g8,red_g9,red_g10)

def alian_red_group2():
  global red_gg1,red_gg2,red_gg3,red_gg4,red_gg5,red_gg6,red_gg7,red_gg8,red_gg9,red_gg10

  red_gg1 = alian(500, 280, 44, 32, alian_r,150)
  red_gg2 = alian(550, 280, 44, 32, alian_r,150)
  red_gg3 = alian(600, 280, 44, 32, alian_r,150)
  red_gg4 = alian(650, 280, 44, 32, alian_r,150)
  red_gg5 = alian(700, 280, 44, 32, alian_r,150)
  red_gg6 = alian(750, 280, 44, 32, alian_r,150)
  red_gg7 = alian(800, 280, 44, 32, alian_r,150)
  red_gg8 = alian(850, 280, 44, 32, alian_r,150)
  red_gg9 = alian(900, 280, 44, 32, alian_r,150)
  red_gg10 = alian(950, 280, 44, 32, alian_r,150)
  
  red_group2.empty()
  red_group2.add(red_gg1,red_gg2,red_gg3,red_gg4,red_gg5,red_gg6,red_gg7,red_gg8,red_gg9,red_gg10)

def alian_blue_group1():
  global blue_g1,blue_g2,blue_g3,blue_g4,blue_g5,blue_g6,blue_g7,blue_g8,blue_g9,blue_g10

  blue_g1 = alian(500, 320, 44, 32, alian_b,100)
  blue_g2 = alian(550, 320, 44, 32, alian_b,100)
  blue_g3 = alian(600, 320, 44, 32, alian_b,100)
  blue_g4 = alian(650, 320, 44, 32, alian_b,100)
  blue_g5 = alian(700, 320, 44, 32, alian_b,100)
  blue_g6 = alian(750, 320, 44, 32, alian_b,100)
  blue_g7 = alian(800, 320, 44, 32, alian_b,100)
  blue_g8 = alian(850, 320, 44, 32, alian_b,100)
  blue_g9 = alian(900, 320, 44, 32, alian_b,100)
  blue_g10 = alian(950, 320, 44, 32, alian_b,100)
  
  blue_group1.empty()
  blue_group1.add(blue_g1,blue_g2,blue_g3,blue_g4,blue_g5,blue_g6,blue_g7,blue_g8,blue_g9,blue_g10)

def alian_blue_group2():
  global blue_gg1,blue_gg2,blue_gg3,blue_gg4,blue_gg5,blue_gg6,blue_gg7,blue_gg8,blue_gg9,blue_gg10

  blue_gg1 = alian(500, 360, 44, 32, alian_b,100)
  blue_gg2 = alian(550, 360, 44, 32, alian_b,100)
  blue_gg3 = alian(600, 360, 44, 32, alian_b,100)
  blue_gg4 = alian(650, 360, 44, 32, alian_b,100)
  blue_gg5 = alian(700, 360, 44, 32, alian_b,100)
  blue_gg6 = alian(750, 360, 44, 32, alian_b,100)
  blue_gg7 = alian(800, 360, 44, 32, alian_b,100)
  blue_gg8 = alian(850, 360, 44, 32, alian_b,100)
  blue_gg9 = alian(900, 360, 44, 32, alian_b,100)
  blue_gg10 = alian(950, 360, 44, 32, alian_b,100)
  
  blue_group2.empty()
  blue_group2.add(blue_gg1,blue_gg2,blue_gg3,blue_gg4,blue_gg5,blue_gg6,blue_gg7,blue_gg8,blue_gg9,blue_gg10)


def start():
  global playing, ending, score, playing_pause, has_run, winning
  playing = True
  ending = False
  score = 0
  playing_pause = False
  has_run = False
  winning = False
  player_init()
  bar_group1_init()
  bar_group2_init()
  bar_group3_init()
  alian_green_group()
  alian_red_group1()
  alian_red_group2()
  alian_blue_group1()
  alian_blue_group2()
  player_life_check()

def pause():
  global playing_pause
  playing_pause = True


btn1 = Button(30, 30, 300, 100, 'EXIT', exit)
btn_toggle_1 = Button(30, 200, 150, 100, f'Alians 1',toggle1)
btn_toggle_2 = Button(180, 200, 150, 100, f'Alians 2', toggle2)
btn_start = Button(30, 300, 300, 100, 'Start', start)
btn_restart = Button(595, 500, 300, 100, 'Restart', start)
vid1.mute()
vid2.mute()
vid1.set_width(300)
vid2.set_width(300)
vid1.set_height(150)
vid2.set_height(150)


def display():
  global btn_toggle_1_state, btn_toggle_2_state, alian_move_type, my_font, winning,text_win,text_end
  window.fill((26,26,34)) #Black background
  green_group.draw(window)
  red_group1.draw(window)
  red_group2.draw(window)
  blue_group1.draw(window)
  blue_group2.draw(window)
  player_group.draw(window)
  player_shot_group.draw(window)
  alian_shot_group.draw(window)
  bar_group1.draw(window)
  bar_group2.draw(window)
  bar_group3.draw(window)
  player_life_group.draw(window)
  
  
  
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

  my_font = pg.font.Font('slkscr.ttf', 30)
  btn1.process(window)

  
  if not playing:
    btn_toggle_1.process(window,btn_toggle_1_state)
    btn_toggle_2.process(window,btn_toggle_2_state)
    btn_start.process(window)
    
    try:
      if toggle1_state == True and vid1.is_playing == False:
        vid1.stop()
        vid1.play()
        vid1.mute()

      elif toggle1_state == True and vid1.is_playing == True:
        vid1.set_width(300)
        vid1.set_height(150)
        vid1.draw_to(window, (30, 400))
      
      if toggle2_state == True and vid2.is_playing == False:
        vid2.stop()
        vid2.play()
        vid2.mute()

      elif toggle2_state == True and vid2.is_playing == True:
        vid2.draw_to(window, (30, 400))
        vid2.set_width(300)
        vid2.set_height(150)
    except:
      pass
  else:
    wall1=pg.draw.rect(window,(235, 247, 247),(1095,0,5,1000))
    wall2=pg.draw.rect(window,(235, 247, 247),(395,0,5,1000))
    my_font = pg.font.Font('slkscr.ttf', 40)
    temp_width = text_score.get_width()
    window.blit(text_score, (745-(temp_width/2),20))
  if ending == True:
    btn_restart.process(window)
    temp_width1 = text_end.get_width()
    window.blit(text_end, (745-(temp_width1/2),400))
  if winning == True:
    btn_restart.process(window)
    temp_width2 = text_win.get_width()
    window.blit(text_win, (745-(temp_width2/2),400))
    
    

def impact(group):
  global score
  try:
    for each in player_shot_group:
      colide= pg.sprite.spritecollide(each, group, False, collided=pg.sprite.collide_mask)  
      if len(colide) >0:
        colide[0].alive=False
        temp_value = colide[0].return_value()
        each.kill()
        score += temp_value
  except: 
    pass


def player_impact():
  global score, playing_pause
  try:
    for each in alian_shot_group:
      colide= pg.sprite.spritecollide(each, player_group, False, collided=pg.sprite.collide_mask)  
      if len(colide) >0:
        playing_pause = True
        each.kill()
  except: 
    pass
  

def bar_impact(group,shot_group):
  try:
    for each in shot_group:
      colide= pg.sprite.spritecollide(each, group, True, collided=pg.sprite.collide_mask)  
      if len(colide) >0:
        each.kill()
  except: 
    pass
  

def alian_move(first,last):
  global move_alian
  if last.rect.x>1050 or first.rect.x<400:  
    move_alian = True
  else:
    move_alian = False
  display() 
  

shot_time = 40
alian_shot_time = 0
group_check = 1
time_left_to_shoot = 0
has_run = False


def alian_shot(group):
  global alian_shot_time
  new_random = random.randint(0,10+1)
  if alian_shot_time>45:
    try:
        times = 0
        for sprites in group:
          times += 1
          if sprites.alive == True:
            if times == new_random:
              tempx, tempy = sprites.x_y_return()
              alian_shot1 = bullet(tempx+18, tempy+32, 10, 28, alian_s1)
              alian_shot_group.add(alian_shot1)
              alian_shot_time = 0
        else:
          return False
    except:
      pass

while True:
    display()
    
  

#v----v-------v-------v-------v----If Playing-----v-------v--------v-------v 
    if playing:
      if shot_time>40:
        time_left_to_shoot = 0
      else:
        time_left_to_shoot = (shot_time-40)*-1
      text_score = my_font.render(f'SCORE:{score}', False, (255, 255, 255))

      if not playing_pause:
        if score == 7500:
          playing_pause == True
          winning = True
        player_impact()
        has_run = False
        shot_time += 1
        alian_shot_time += 1
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

        check = alian_shot(blue_group2)
        if check == False:
          check = alian_shot(blue_group1)
          if check == False:
            check = alian_shot(red_group2)
            if check == False:
              check = alian_shot(red_group1)
              if check == False:
                check = alian_shot(green_group)
        try:
          for each in player_shot_group:
            each.move_play()
            if each.rect.y <0:
              each.kill()
          for each in alian_shot_group:
            each.move_alian()
            if each.rect.y > 950:
              each.kill()
        except:
          pass
      
        impact(green_group)      
        impact(red_group1)
        impact(red_group2)
        impact(blue_group1)
        impact(blue_group2)
        bar_impact(bar_group1,player_shot_group)
        bar_impact(bar_group2,player_shot_group)
        bar_impact(bar_group3,player_shot_group)
        bar_impact(bar_group1,alian_shot_group)
        bar_impact(bar_group2,alian_shot_group)
        bar_impact(bar_group3,alian_shot_group)
      
        #if alian_move_type == False:
        alian_move(green_g1,green_g10)
        if player.rect.x > 1050:
          player.back()
          display()
        elif player.rect.x < 400:
          player.back()
          display()
      else:
        if has_run == False:
          has_run = True
          player_life -= 1
          try:
            for each in player_shot_group:
              each.kill()
            for each in alian_shot_group:
              each.kill()
          except:
            pass
          pg.display.update()
          pg.time.delay(500)
          player_init()
          pg.sprite.Group(green_group).update(alian_move_type, move_alian,True)
          pg.sprite.Group(red_group1).update(alian_move_type, move_alian,True)
          pg.sprite.Group(red_group2).update(alian_move_type, move_alian,True)
          pg.sprite.Group(blue_group1).update(alian_move_type, move_alian,True)
          pg.sprite.Group(blue_group2).update(alian_move_type, move_alian,True)
          display()
          pg.display.update()
          pg.time.delay(500)
          player_life_check()
          display()
          if not player_life <= 0:
            playing_pause = False
            has_run == False
          elif winning == True:
            text_win = my_font.render(f'WINNER', False, (255, 255, 255))
          else:
            ending = True
            text_end = my_font.render(f'GAME OVER', False, (255, 255, 255))

          
          
          
#^-----^----^-----^------^--------If Playing-----^----^-------^------^-----^  


    for event in pg.event.get():
      if event.type == pg.QUIT:# if user  QUIT then the screen will close 
        exit()
    
    pg.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
