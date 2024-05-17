import  random

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass
    def distance(self):
        return self.x


class Dice:
    def __int__(self):
        pass
    
    def roll(self):
       x= random.randint(1,6)
       y= random.randint(1,6)
       return (x,y)

       
    
    

point=Point(3,4)
print(point.distance())

d=Dice()

print(d.roll())