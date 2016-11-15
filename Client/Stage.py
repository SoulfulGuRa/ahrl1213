import game_framework
from pico2d import *
import Background
import TestScene
import Player
import Tile

name = "Stage"

def enter():
   global background, player, tile
   background = Background.Background()
   player = Player.Player()
   tile = []
   #tile = Tile.Tile(0, 0, 0, 0)
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

def draw():
    clear_canvas()

    background.draw()
    player.draw()
    for x in range(len(tile)):
        tile[x].draw()

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
        elif event.type == SDL_KEYDOWN:
            background.handle_event(event)
            player.handle_event(event)

def pause(): pass


def resume(): pass




