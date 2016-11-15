from pico2d import *
from Static import Static

class Background:
    def __init__(self):
        global ScrollX
        self.background = load_image('BackGround.png')
        self.backcastle = load_image('BackCastle.png')
        self.backforest = load_image('BackForest.png')
        self.backtree1 = load_image('BackTree1.png')
        self.backtree2 = load_image('BackTree2.png')
        self.LeftKey = False
        self.RightKey = False
        ScrollX = Static

    def update(self):
        pass

    def draw(self):
        self.background.draw(400, 300, 800, 600)
        self.backcastle.draw(700 + ScrollX.ScrollX * 0.03, 330, 200, 370)

        for x in range(0, 3):
            self.backforest.draw((300 + ScrollX.ScrollX * 0.05) + 900 * x, 150, 900, 220)

        for x in range(0, 200):
            if 0 == x % 2:
                self.backtree1.draw((ScrollX.ScrollX * 0.2) + 150 * x, 240, 180, 230)
            else:
                self.backtree1.draw((ScrollX.ScrollX * 0.2) + 150 * x, 240, 180, 260)

        for x in range(0, 200):
            if 0 == x % 2:
                self.backtree2.draw((ScrollX.ScrollX * 0.4) + 250 * x, 230, 190, 330)
            else:
                self.backtree2.draw((ScrollX.ScrollX * 0.4) + 250 * x, 240, 190, 350)

        for x in range(0, 200):
            if 0 == x % 2:
                self.backtree2.draw((ScrollX.ScrollX * 0.6) + 300 * x, 240, 210, 420)
            else:
                self.backtree2.draw((ScrollX.ScrollX * 0.6) + 300 * x, 260, 210, 450)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            print('LeftDown')
            self.LeftKey = True
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            print('LeftUp')
            self.LeftKey = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            print('RightDown')
            self.RightKey = True
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            print('RightUp')
            self.RightKey = False