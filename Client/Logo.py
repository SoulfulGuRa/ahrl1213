import game_framework
from pico2d import *


name = "Logo"
main = None
start = None
option = None
esc = None

def enter():
    global main, start, option, esc

    open_canvas()

    main = load_image('Main.png')
    start = load_image('Start.png')
    option = load_image('Option.png')
    esc = load_image('Exit.png')

def exit():
    global main, start, option, esc
    del(main)
    del(start)
    del(option)
    del(esc)

def update():
    handle_events()
    delay(0.01)

def draw():
    global main, start, option, esc
    clear_canvas()

    main.draw(400, 300)
    start.draw(400, 250)
    option.draw(400, 200)
    esc.draw(400, 150)

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def pause(): pass


def resume(): pass




