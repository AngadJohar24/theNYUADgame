class Ship:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx=0
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
        self.y-=1
        
class Obstacle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def display(self):
        rect(self.x,self.y,self.w,self.h)
                
s=playerShip(150,700,20,20)
o=Obstacle(100,100,25,85)

def setup():
    size(400,800)
    
def draw():
    background(255)
    s.display()
    o.display()
    s.update()
    
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
        
    
        
    
