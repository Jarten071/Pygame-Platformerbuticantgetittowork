import boards as Boards
import cameramanager as cam
from timer import Timer
colors = {
    "red":   (255,0,  0  ),
    "green": (0,  255,0  ),
    "blue":  (0,  0,  255),
}
class create():
    def __init__(self, x, y, xl, yl, xv = 0, yv = 0, gr = False, st = 0, wj = False):
        self.x = x
        self.y = y
        self.xl = xl
        self.yl = yl
        self.xv = xv
        self.yv = yv
        self.gr = gr
        self.st = st
        self.wj = wj
        self.w = None
        self.speed = 6
        self.acc = 1
        self.decel = 0.5
        self.dyndecel = 1
        self.jumppower = -18
        self.gravity = 7
        self.dashes = 1
        self.dashstate = False
        self.dashleave = True
        self.dashlength = 10
        self.dashcooldown = 2
        self.dashspeed = 18
        self.dashlist = [False, False, False, False]
        self.dashslow = 1
        self.color = colors["red"]

    def die(self, level):
        self.x = 500
        self.x = 1000 / 2
        self.y = level.height
        self.yv = -30
        self.xv = 0
        self.dashes = 1
        

    def jump(self):
        self.yv = self.jumppower
        self.gr = False
        self.dashslow = 1
        self.xv * 1.2
        self.dashslow = 1
        if self.dashleave or self.dashstate:
            print("Dash Cancel")
            if not self.xv == 0:
                self.xv = abs(self.xv)/ self.xv * 24
                if self.dashlist[3] == True:
                    print("Hyper")
                    self.yv = -13
                    self.xv *= 3

    def walljump(self, wallcheck):
        if wallcheck[0] and wallcheck[1]:
            self.yv = self.jumppower
        elif wallcheck[0]:
            self.xv = -7
            self.yv = self.jumppower
        elif wallcheck[1]:
            self.xv = 7
            self.yv = self.jumppower

        if self.dashleave or self.dashstate:
            if self.dashlist[0]:
                print("Dash Cancel")
                self.yv *= 1.2
                self.xv *= 1.5
                
           
    def dash(self):
        input = ["up", "left", "right", "down", "jump", "dash"]
        self.dashes -= 1
        self.dashslow = 2
        for i in range(4):
            if Boards.getP(input[i]):
                self.dashlist[i] = True
        if self.dashlist == [False, False, False, False]:
            self.dashlist[2] = True
        
    def resetDash(self):
        self.dashes = 1
        self.dashstate = False
        self.dashleave = False
        Timer.set("dashleave", True)
        Timer.set("dash", True)
        Timer.set("dashcool", True)
