import game_framework
from pico2d import *
import Background
import TestScene
import Player
import Tile
from Static import Static

name = "Stage"

def enter():
   global background, player, tile
   global ScrollX
   ScrollX = Static
   background = Background.Background()
   player = Player.Player()
   tile = []
   tile.append(Tile.Tile(3, 6, 3, 2))
   tile.append(Tile.Tile(3, 6, 8, 5))
   for y in range(0, 2):
       for x in range(0, 200):
           if y == 1:
               a = 2
               b = 3
           else:
               a = 3
               b = 6
           tile.append(Tile.Tile(a, b, x, y))

def exit():
    global background, player, tile
    del(background)
    del(player)
    del(tile)

def update():
    background.update()
    player.update()

    for x in range(len(tile)):
        collide(player, tile[x])
        #if collide(player, tile[x]):
            #tile[x].setboxdraw(True)
        #else:
            #tile[x].setboxdraw(False)

def draw():
    clear_canvas()

    background.draw()

    for x in range(len(tile)):
        tile[x].draw()

    player.draw()

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            print('Enter TestScene')
            game_framework.change_state(TestScene)
        elif event.type == SDL_KEYUP:
            background.handle_event(event)
            player.handle_event(event)
            for x in range(len(tile)):
                tile[x].handle_event(event)
        elif event.type == SDL_KEYDOWN:
            background.handle_event(event)
            player.handle_event(event)
            for x in range(len(tile)):
                tile[x].handle_event(event)

#def collide(a, b):
   # left_a, bottom_a, right_a, top_a = a.get_bb()
    #left_b, bottom_b, right_b, top_b = b.get_bb()

   # if left_a > right_b:
      #  return False
   # if right_a < left_b:
     #   return False
    #if top_a < bottom_b:
     #   return False
   # if bottom_a > top_b:
       # return False

    #return True

def collide(a, b):
    destx, desty, destr = a.get_info()
    sourx, soury, sourr = b.get_info()

    fx = abs(sourx - destx)
    fy = abs(soury - desty)

    collx = (destr + sourr) - fx
    colly = (destr + sourr) - fy

    if collx < 0 or colly <0:
        return

    if desty < soury:
        if destx < sourx:
            if collx > colly:
                a.setpos(destx - ScrollX.ScrollX, soury - sourr - destr + 20)
                a.colcheckright(False)
                print('1')
            else:
                a.setpos(sourx - sourr - destr - ScrollX.ScrollX, desty + 20)
                a.colcheckright(True)
                print('2')
        else:
            if collx > colly:
                a.setpos(destx - ScrollX.ScrollX, soury - sourr - destr + 20)
                a.colcheckleft(False)
                print('3')
            else:
                a.setpos(sourx + sourr + destr - ScrollX.ScrollX, desty + 20)
                a.colcheckleft(True)
                print('4')
    else:
        if destx < sourx:
            if collx > colly:
                a.setpos(destx - ScrollX.ScrollX, soury + sourr + destr + 20)
                a.colcheckright(False)
                print('5')
            else:
                a.setpos(sourx - sourr - destr - ScrollX.ScrollX, desty + 20)
                a.colcheckright(True)
                print('6')
        else:
            if collx > colly:
                a.setpos(destx - ScrollX.ScrollX, soury + sourr + destr + 20)
                a.colcheckleft(False)
                print('7')
            else:
                a.setpos(sourx + sourr + destr - ScrollX.ScrollX, desty + 20)
                a.colcheckleft(True)
                print('8')

    return



def pause(): pass


def resume(): pass




