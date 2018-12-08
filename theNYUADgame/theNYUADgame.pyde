class Ship:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx=0
    def display(self):
        ellipse(self.x,self.y,self.w,self.h)
    def update(self):
        self.x+=self.vx
s=Ship(150,500,20,20)
def setup():
    background(255)
    size(300,600)
def draw():
    s.display()
    
