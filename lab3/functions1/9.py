import math
def vol(radius):
    v=4/3*math.pi*(int(radius))**3
    print(f"{v:.2f}")
n=input()
vol(n)