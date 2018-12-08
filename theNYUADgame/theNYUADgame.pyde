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
s=Ship(150,500,20,20)
def setup():
    #background(255)
    size(300,600)
def draw():
    background(255)
    s.display()
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
        
    
        
    
