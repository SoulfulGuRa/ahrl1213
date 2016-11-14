from pico2d import *
from Static import Static

class Tile:
    def __init__(self, row, col, x, y):
        global ScrollX
        ScrollX = Static
        self.Image = load_image('MapTile.png')
        self.row = row
        self.col = col
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self):
        #for x in range(0, 32):
            #for y in range(0, 2):
                #self.Image.clip_draw(
                    #self.col * 16, # 이미지의 left
                    #self.row * 16, # 이미지의 bottom
                    #16, # 이미지의 사용할 크기
                    #16, # 이미지의 사용할 크기
                    #(ScrollX.ScrollX) + 25 + self.x * 50, # 그림 위치
                    #25 + self.y * 50 , # 그림 위치
                    #50, # 그림 너비
                    #50) # 그림 너비
        self.Image.clip_draw(
            self.col * 16,  # 이미지의 left
            self.row * 16,  # 이미지의 bottom
            16,  # 이미지의 사용할 크기
            16,  # 이미지의 사용할 크기
            (ScrollX.ScrollX) + 25 + self.x * 50,  # 그림 위치
            25 + self.y * 50,  # 그림 위치
            50,  # 그림 너비
            50)  # 그림 너비

    def handle_event(self, event):
        pass
