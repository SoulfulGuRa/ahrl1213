import game_framework
from pico2d import *
import Player
import Scarab

name = "TestScene"

def enter():
   global player, scarab
   player = Player.Player()
   scarab = Scarab.Scarab(600, 20)

def exit():
    global player, scarab
    del(player)
    del(scarab)

def update():
    player.update()
    scarab.update()

    delay(0.05)

def draw():
    clear_canvas()

    scarab.draw()
    player.draw()

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYUP:
            player.handle_event(event)
        elif event.type == SDL_KEYDOWN:
            player.handle_event(event)

def pause(): pass


def resume(): pass




