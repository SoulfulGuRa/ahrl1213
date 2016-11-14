import game_framework
from pico2d import *
import Stage
import Maptool

name = "Logo"
main = None
start = None
option = None
esc = None
select = None
PosY = 250

def enter():
    global main, start, option, esc, select

    open_canvas()

    main = load_image('Main.png')
    start = load_image('Start.png')
    option = load_image('Option.png')
    esc = load_image('Exit.png')
    select = load_image('Select.png')

def exit():
    global main, start, option, esc, select
    del(main)
    del(start)
    del(option)
    del(esc)
    del(select)

def update():
    pass
def draw():
    global main, start, option, esc, select
    global PosY
    clear_canvas()

    main.draw(400, 300)
    start.draw(330 + 193 / 2, 250)
    option.draw(330 + 134 / 2, 200)
    esc.draw(330 + 77 / 2, 150)
    select.draw(270, PosY)

    update_canvas()

def handle_events():
    global PosY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if PosY == 150:
                PosY = 150
            else:
                PosY -= 50
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if PosY == 250:
                PosY = 250
            else:
                PosY += 50
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            if PosY == 150:
                game_framework.quit()
            elif PosY == 200:
                print("Enter MapTool")
                game_framework.change_state(Maptool)
            elif PosY == 250:
                print("Enter Stage")
                game_framework.change_state(Stage)

def pause(): pass


def resume(): pass




