import game_framework
from pico2d import *
import Background
import TestScene
import Player

name = "Stage"

def enter():
   global background, player
   background = Background.Background()
   player = Player.Player()

def exit():
    global background, player
    del(background)
    del(player)

def update():
    background.update()
    player.update()
    delay(0.05)
    # Delay 부분 없애자 타임값 가져와서
    # 루프 수정

def draw():
    clear_canvas()

    background.draw()
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
        elif event.type == SDL_KEYDOWN:
            background.handle_event(event)
            player.handle_event(event)

def pause(): pass


def resume(): pass




