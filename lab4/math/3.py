#write a python program to calculate the area of regular polygon
import math
def area(sides,length):
    a=(sides*length**2)/(4*math.tan(math.pi/sides))
    return a
sides=int(input())
length=float(input())
a=area(sides,length)
print(f"{a:.0f}")