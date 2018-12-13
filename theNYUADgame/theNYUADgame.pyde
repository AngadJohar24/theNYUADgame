import os
path=os.getcwd()+'/images/'

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
        image(s.img2, self.x-self.w/2, self.y-self.w/2, 200, 215)

    def update(self):
        if self.keyCommand[LEFT]:
            self.vx=-3
        elif self.keyCommand[RIGHT]:
            self.vx=3
        else:
            self.vx=0
        self.x+=self.vx
        
class playerShip(Ship):
    
    def __init__(self, x, y, w, h):
        Ship.__init__(self, x, y, w, h)
        self.img2=loadImage(path+'cstresh2.png')
        self.keyCommand={LEFT:False, RIGHT:False}
        
    def update(self):
        if self.keyCommand[LEFT]:
            if self.x-(self.w/2)>=0:
                self.vx=-5
            else:
                self.vx=0
            
        elif self.keyCommand[RIGHT]:
            if self.x+(self.w/2)<=625:
                self.vx=5
            else:
                self.vx=0

        else:
            self.vx=0
        self.x+=self.vx
        g.g+=g.vg
        g.gobj+=g.vg
        
    def distance(self, target):
        return ((self.x - target.x)**2 + (self.y - target.y)**2)**0.5
    
    def display(self):
        self.update()
        ellipse(self.x,self.y,self.w,self.h)
        image(self.img2, self.x-self.w/2, self.y-self.w/2, 200, 215)
                    
class Obstacle:
    
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.img4=loadImage(path+'mfa2.png')
    
    def update(self):
        self.y-=g.vg
        if (g.s.x>=self.x-g.s.w/2 and g.s.x<=self.x+self.w+g.s.w/2) and (g.s.y-g.s.w/2<=self.y+self.h and g.s.y+g.s.w/2>=self.y):
            g.vg=0
            g.__init__(625,728)
                
    def display(self):
        self.update()
        rect(self.x,self.y,self.w,self.h)
        image(self.img4, self.x, self.y)
        

class Coin(Obstacle):
    
    def __init__(self,x,y,w,h):
        Obstacle.__init__(self,x,y,w,h)
        self.img3=loadImage(path+'mealswipe.png')
        
    def update(self):
        self.y-=g.vg  
          
    def display(self):
        self.update()
        if g.s.distance(self)>self.w/2+g.s.w/2 and self.y<g.s.y:
            ellipse(self.x,self.y,self.w,self.h)
            image(self.img3, self.x-self.w/2, self.y-self.w/2)
                        
    

class Game:
    
    def __init__(self,w,h):
        self.x=0
        self.w=w
        self.g=0
        self.gobj=0
        self.vg=-6
        self.h=h
        self.img=loadImage(path+'background.png')
        self.s=playerShip(self.w/2-100, self.h-100, 200, 200)
        self.o=Obstacle(100,-500,83,500)
        self.c=Coin(200, 100, 50, 50)
        
    def display(self):
        if self.g<=-self.h:
            self.g=0
        image(self.img, 0, -self.g)
        image(self.img, 0, 0, self.w, -self.g, 0, self.h+self.g, self.w, self.h)
        self.s.display()
        self.o.display()
        self.c.display()
        
             
g=Game(625,728)

def setup():
    size(625,728)
    
def draw():
    noFill()
    noStroke()
    background(255)
    g.display()
    
def keyPressed():
    if keyCode==LEFT:
        g.s.keyCommand[LEFT]=True
    elif keyCode==RIGHT:
        g.s.keyCommand[RIGHT]=True
        
def keyReleased():
    if keyCode==LEFT:
        g.s.keyCommand[LEFT]=False
    elif keyCode==RIGHT:
        g.s.keyCommand[RIGHT]=False
        
     
        
    
