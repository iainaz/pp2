#write a python program to calvulate the area of a parallelogram
import math
def area(length,height):
    a=length*height
    return a
length=int(input())
height=float(input())
a=area(length,height)
print(f"{a:.1f}")