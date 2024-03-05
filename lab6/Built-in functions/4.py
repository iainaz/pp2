#Write a Python program that invoke square root function after specific milliseconds
import time
import math
def delayed_sqrt(num,ms):
    sec=ms/1000
    time.sleep(sec)
    return math.sqrt(num)
num=25
ms=2000
print(delayed_sqrt(num,ms))