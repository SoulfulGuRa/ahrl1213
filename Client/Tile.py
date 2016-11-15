from pico2d import *
from Static import Static

class Tile:
    image = None

    def __init__(self, row, col, x, y):
        global ScrollX
        ScrollX = Static
        self.Image = load_image('MapTile.png')
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.boxdraw = False

    def update(self):
        pass

    def draw(self):
        self.Image.clip_draw(
            self.col * 16,  # 이미지의 left
            self.row * 16,  # 이미지의 bottom
            16,  # 이미지의 사용할 크기
            16,  # 이미지의 사용할 크기
            (ScrollX.ScrollX) + 25 + self.x * 50,  # 그림 위치
            25 + self.y * 50,  # 그림 위치
            50,  # 그림 너비
            50)  # 그림 너비
        if self.boxdraw == True:
            draw_rectangle(*self.get_bb())

    def get_info(self):
        return (ScrollX.ScrollX) + (50 * self.x) + 25, (50 * self.y) + 25, 25

    def get_bb(self):
        return (ScrollX.ScrollX) + (self.x * 50), (self.y * 50), (ScrollX.ScrollX) + (self.x * 50) + 50, (self.y * 50) + 50

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_TAB:
            self.boxdraw = True
        elif event.type == SDL_KEYUP and event.key == SDLK_TAB:
            self.boxdraw = False

    def setboxdraw(self, boxdraw):
        self.boxdraw = boxdraw


