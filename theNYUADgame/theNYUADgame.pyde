import os
path=os.getcwd()+'/'

class Ship:
    def __init__(self, x, y, w, h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx=0
        self.keyCommand={LEFT:False, RIGHT:False}
        
    def display(self):
        image(s.img2, self.x-self.w/2, self.y-self.w/2, 200, 215)
        ellipse(self.x,self.y,self.w,self.h)

                
class playerShip(Ship):
    def __init__(self, x, y, w, h):
        Ship.__init__(self, x, y, w, h)
        self.img2=loadImage(path+'cstresh.png')
        self.keyCommand={LEFT:False, RIGHT:False}
        
    def update(self):
        if self.keyCommand[LEFT] and self.x+self.w/2>self.w:
            self.vx=-3
        elif self.keyCommand[RIGHT] and self.x+self.w/2<400:
            self.vx=3
        else:
            self.vx=0
        self.x+=self.vx
        g.g+=g.vg
        g.gobj+=g.vg
        
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

class Coin(Obstacle):
    def __init__(self,x,y,w,h):
        Obstacle.__init__(self,x,y,w,h)
        
    def display(self):
        ellipse(self.x,self.y,self.w,self.h)
                        
class Game:
    def __init__(self,w,h):
        self.x=0
        self.w=w
        self.g=0
        self.gobj=0
        self.vg=-2
        self.h=h
        self.img=loadImage(path+'background.png')
        
    def display(self):
        if self.g<=-728:
            self.g=0
        image(self.img, 0, -self.g)
        image(self.img, 0, 0, self.w, -self.g, 0, self.h+self.g, self.w, self.h)
        s.display()
        o.display()
        
    def update(self):
        if s.distance(c)<=s.w/2+c.w/2:
            #add condition
        c.y-=g.vg
        o.y-=g.vg
        if (s.x>=o.x-s.w/2 and s.x<=o.x+o.w+s.w/2) and (s.y<=o.y+o.h and s.y>=o.y):
            g.vg=0
             
g=Game(625,728)
s=playerShip(350,600,200,200)
o=Obstacle(100,100,25,85)
c=Coin(200, 100, 10, 10)

def setup():
    size(400,728)
    
def draw():
    background(255)
    g.display()
    c.display()
    g.update()
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
        
     
        
    
