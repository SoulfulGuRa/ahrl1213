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
   tile = Tile.Tile(0, 0, 0, 0)

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
    tile.draw()

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




