import math
def histogram(nums):
    for x in nums:
        print('*'*x)
n=input()
nlist=[int(x) for x in n.split()]
histogram(nlist)