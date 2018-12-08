import os
path=os.getcwd()+'/'
class Ship:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx=0
        self.vy=-3
        self.keyCommand={LEFT:False, RIGHT:False}
    def display(self):
        ellipse(self.x,self.y,self.w,self.h)
    def update(self):
        if self.keyCommand[LEFT]:
            self.vx=-2
        elif self.keyCommand[RIGHT]:
            self.vx=2
        else:
            self.vx=0
        self.x+=self.vx
        self.y+=self.vy
        
class playerShip(Ship):
    def __init__(self, x, y, w, h):
        Ship.__init__(self, x, y, w, h)
        self.keyCommand={LEFT:False, RIGHT:False}
    def update(self):
        if self.keyCommand[LEFT]:
            self.vx=-2
        elif self.keyCommand[RIGHT]:
            self.vx=2
        else:
            self.vx=0
        self.x+=self.vx
        self.y+=self.vy
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
        
class Obstacle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def display(self):
        rect(self.x,self.y,self.w,self.h)

class Game:
    def __init__(self,w,h):
        self.x=0
        self.w=w
        self.h=h
        self.img=loadImage(path+'background.png')
    def display(self):
        image(self.img, 0,0)
    def update(self):
        if s.distance(o)<=(s.w/2)+(o.h) or s.distance(o)<=(s.w/2)+(o.w):
            s.distance(o)==(s.w/2)+(o.h)
            s.vy=0
        
g=Game(625,728)
s=playerShip(150,700,20,20)
o=Obstacle(100,100,25,85)


def setup():
    size(400,800)
    
def draw():
    background(255)
    g.display()
    s.display()
    o.display()
    s.update()
    g.update()
    
def keyPressed():
    if keyCode==LEFT:
        s.keyCommand[LEFT]=True
    elif keyCode==RIGHT:
        s.keyCommand[RIGHT]=True
        
def keyReleased():
    if keyCode==LEFT:
        s.keyCommand[LEFT]=False
    elif keyCode==RIGHT:
        s.keyCommand[RIGHT]=False
        
    
        
    
