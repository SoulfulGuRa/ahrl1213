from pico2d import *
from Static import Static

class Player:
    IDLE, RUN, ATTACK, DOWNATKACK, JUMP, DOWN, WINPOSE, ENTER = 15, 14, 13, 12, 11, 10, 0, 1

    def handle_idle(self):
        self.frame = 0

    def handle_run(self):
        self.frame = (self.frame + 1) % 6

    def handle_attack(self):
        self.frame = (self.frame + 1) % 5
        if(self.frame == 4):
            self.Attack = False

    def handle_downattack(self):
        pass

    def handle_jump(self):
        pass

    handle_state = {
        IDLE: handle_idle,
        RUN: handle_run,
        ATTACK: handle_attack,
        DOWNATKACK: handle_downattack,
        JUMP: handle_jump
    }

    def __init__(self):
        global ScrollX
        ScrollX = Static
        self.mapscale = 10000
        self.x, self.y = 100, 150
        self.frame = 0
        self.state = self.IDLE
        self.colleft = False
        self.colright = False
        self.boxdraw = False
        self.Attack = False
        self.LeftKey = False
        self.RightKey = False
        self.LeftCheck = False
        self.RightCheck = True
        self.imageLeft = load_image('L_Player.png')
        self.imageRight = load_image('R_Player.png')

    def update(self):
        if self.LeftKey == True:
            if(self.x > 400 and self.mapscale - 400 > self.x):
                if self.colleft == False:
                    ScrollX.ScrollX += 10

            if(ScrollX.ScrollX > 0):
                ScrollX.ScrollX = 0

            self.x -= 10

            if(self.x < 0):
                self.x = 0

        if self.RightKey == True:
            if(self.x > 400 and self.mapscale - 400 > self.x):
                if self.colright == False:
                    ScrollX.ScrollX -= 10

            if(ScrollX.ScrollX < -(self.mapscale - 800)):
                ScrollX.ScrollX = -(self.mapscale - 800)

            self.x += 10

            if(self.x > self.mapscale):
                self.x = self.mapscale

        if(self.LeftKey == True):
            self.state = self.RUN
        if(self.RightKey == True):
            self.state = self.RUN
        if(self.Attack == True):
            self.state = self.ATTACK
        if(self.LeftKey == False and self.RightKey == False and
                   self.Attack == False):
            self.state = self.IDLE

        self.handle_state[self.state](self)

    def draw(self):
        if(self.LeftCheck == True):
            self.imageLeft.clip_draw(self.frame * 85, self.state * 64, 85, 64, self.x + ScrollX.ScrollX, self.y, 200, 200)
        else:
            self.imageRight.clip_draw(self.frame * 85, self.state * 64, 85, 64, self.x + ScrollX.ScrollX, self.y, 200, 200)

        if self.boxdraw == True:
            draw_rectangle(*self.get_bb())

    def get_info(self):
        # x, y, radius
        return (ScrollX.ScrollX) + self.x, self.y - 20, 30

    def get_bb(self):
        return ((ScrollX.ScrollX) + (self.x) - 30, (self.y - 20) - 30, (ScrollX.ScrollX) + (self.x) + 30, (self.y - 20) + 30)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            self.LeftKey = True
            self.LeftCheck = True
            self.RightCheck = False
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            self.LeftKey = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            self.RightKey = True
            self.RightCheck = True
            self.LeftCheck = False
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            self.RightKey = False

        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            self.Attack = True

        if event.type == SDL_KEYDOWN and event.key == SDLK_TAB:
            self.boxdraw = True
        elif event.type == SDL_KEYUP and event.key == SDLK_TAB:
            self.boxdraw = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            self.y += 10
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            self.y -= 10

    def setpos(self, posx, posy):
        self.x = posx
        self.y = posy

    def colcheckleft(self, col):
        self.colleft = col

    def colcheckright(self, col):
        self.colright = col
