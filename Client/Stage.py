import game_framework
from pico2d import *

name = "Stage"

background = None
backcastle = None
backforest = None
backtree1 = None
backtree2 = None

ScrollX = 0
ScrollY = 0

LeftKey = False
RightKey = False

def enter():
    global background, backcastle, backforest, backtree1, backtree2
    global ScrollX, ScrollY
    background = load_image('BackGround.png')
    backcastle = load_image('BackCastle.png')
    backforest = load_image('BackForest.png')
    backtree1 = load_image('BackTree1.png')
    backtree2 = load_image('BackTree2.png')

def exit():
    global background, backcastle, backforest, backtree1, backtree2
    del(background)
    del(backcastle)
    del(backforest)
    del(backtree1)
    del(backtree2)

def update():
    global LeftKey, RightKey
    global ScrollX, ScrollY
    handle_events()
    if LeftKey == True:
        ScrollX += 10
    if RightKey == True:
        ScrollX -= 10
    delay(0.01)

def draw():
    global ScrollX, ScrollY
    clear_canvas()

    background.draw(400, 300, 800, 600)
    backcastle.draw(700 + ScrollX * 0.01, 330, 200, 370)

    for x in range(0, 3):
        backforest.draw((300 + ScrollX * 0.02) + 900 * x, 110, 900, 220)

    for x in range(0, 200):
        if 0 == x % 2:
            backtree1.draw((ScrollX * 0.1) + 150 * x, 190, 180, 230)
        else:
            backtree1.draw((ScrollX * 0.1) + 150 * x, 190, 180, 260)

    for x in range(0, 200):
        if 0 == x % 2:
            backtree2.draw((ScrollX * 0.2) + 250 * x, 190, 190, 330)
        else:
            backtree2.draw((ScrollX * 0.2) + 250 * x, 190, 190, 350)

    for x in range(0, 200):
        if 0 == x % 2:
            backtree2.draw((ScrollX * 0.3) + 300 * x, 190, 210, 420)
        else:
            backtree2.draw((ScrollX * 0.3) + 300 * x, 190, 210, 450)

    update_canvas()

def handle_events():
    global LeftKey, RightKey
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            print('LeftDown')
            LeftKey = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            print('LeftUp')
            LeftKey = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            print('RightDown')
            RightKey = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            print('RightUp')
            RightKey = False

def pause(): pass


def resume(): pass




