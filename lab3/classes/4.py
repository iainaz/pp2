'''Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points'''
import math
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        print(f"Coordinates:({self.x}, {self.y})")
    def move(self,xn,yn):
        self.x=xn
        self.y=yn
    def dist(self,secpoint):
        distance = math.sqrt((self.x-secpoint.x)**2+(self.y-secpoint.y)**2)
        return distance
fpoint=Point(1,2)
spoint=Point(9,10)
fpoint.show()
spoint.show()
distt=fpoint.dist(spoint)
print(distt)