import game_framework
from pico2d import *
import Background
import Tile
from Static import Static

name = "Stage"

def enter():
   global background, tile
   global ScrollX, LeftDown, RightDown
   global tileCntX, tileCntY, tileCX, tileCY, tileindex
   ScrollX = Static
   background = Background.Background()
   LeftDown = False
   RightDown = False
   tile = []
   tileCntX = 16
   tileCntY = 12
   tileCX = 50
   tileCY = 50
   for y in range(0, tileCntY):
       for x in range(0, tileCntX):
           tile.append(Tile.Tile(0, 0, x, y))

def exit():
    global background, tile
    del(background)
    del(tile)

def update():
    background.update()

    for x in range(len(tile)):
        tile[x].update()

    if LeftDown == True:
        ScrollX.ScrollX += 10
    if RightDown == True:
        ScrollX.ScrollX -= 10


def draw():
    clear_canvas()

    background.draw()

    for x in range(len(tile)):
        tile[x].draw()

    update_canvas()

def handle_events():
    global ScrollX, LeftDown, RightDown
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            LeftDown = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            RightDown = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            LeftDown = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            RightDown = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mapedit(event.x, event.y)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_RIGHT:
            pass

def mapedit(mouseX, mouseY):
    pass

def pause():
    pass

def resume():
    pass




