from pico2d import *
from Static import Static

class Scarab:
    RUN, DIE = 1, 0

    def __init__(self, x, y):
        global ScrollX
        ScrollX = Static
        self.x, self.y = x, y
        self.frame = 0
        self.state = self.RUN
        self.LeftCheck = True
        self.RightCheck = False
        self.runframe = 0
        self.imageLeft = load_image('L_Scarab.png')
        self.imageRight = load_image('R_Scarab.png')

    def update(self):
        if self.LeftCheck == True:
            self.x -= 5
            self.runframe += 1
            self.frame = (self.frame + 1) % 4
            if(self.runframe > 15):
                self.LeftCheck = False
                self.RightCheck = True
                self.runframe = 0

        if self.RightCheck == True:
            self.x += 5
            self.runframe += 1
            self.frame = (self.frame + 1) % 4
            if(self.runframe > 15):
                self.RightCheck = False
                self.LeftCheck = True
                self.runframe = 0

    def draw(self):
        if(self.LeftCheck == True):
            self.imageLeft.clip_draw(self.frame * 26, self.state * 16, 26, 16, self.x + ScrollX.ScrollX, self.y, 50, 50)
        else:
            self.imageRight.clip_draw(self.frame * 26, self.state * 16, 26, 16, self.x + ScrollX.ScrollX, self.y, 50, 50)

