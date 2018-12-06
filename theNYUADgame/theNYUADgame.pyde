class Ship:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx=0
    def display(self):
        ellipse(x,y,w,h)
    def update(self):
        self.x+=self.vx
class myShip(Ship):
    def __init__(self, x, y, w, h):
        Ship.__init__(self, x, y, w, h)
        self.keyStuff={LEFT:False, RIGHT:False}
    def move(self):
        if 
def keyPressed():
    if keyCode == LEFT:
        [LEFT] = True
    elif keyCode == RIGHT:
        [RIGHT] = True
        
