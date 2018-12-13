
<<<<<<< HEAD
import os
=======
>>>>>>> ba840e11724d715c4cf0e858957a73e06968f6d0

import os, random

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
        image(g.s.img2, self.x-self.w/2, self.y-self.w/2, 90, 96)

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
        self.img2=loadImage(path+'cstresh5.png')
        self.keyCommand={LEFT:False, RIGHT:False}
        
    def update(self):
        if self.keyCommand[LEFT]:
            if self.x-(self.w/2)>=0:
                self.vx=-5
            else:
                self.vx=0
            
        elif self.keyCommand[RIGHT]:
            if self.x+(self.w/2)<=g.w:
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
        image(self.img2, self.x-self.w/2, self.y-self.w/2, 113, 120)
                    
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
            g.__init__(612, 800)

                
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
        self.img=loadImage(path+'background4.png')
        self.s=playerShip(self.w/2-100, self.h-100, 120, 120)
        self.c=Coin(200, 100, 50, 50)
        self.oList=[]
        x=10
        y=100
        for o in range(50):
            for o1 in range(2):
                self.oList.append(Obstacle(x, y, 83, 500))
                x+=180+random.randint(10, 200)
            y-=1000
            x=10     
                      
    def display(self):
        if self.g<=-self.h:
            self.g=0
        image(self.img, 0, -self.g)
        image(self.img, 0, 0, self.w, -self.g, 0, self.h+self.g, self.w, self.h)
        self.s.display()
        self.c.display()
        for o in range(100):
            self.oList[o].display()
                        
g=Game(612,800)

def setup():
    size(612,800)
    
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
        
     
        
    
