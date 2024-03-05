#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
def multiply_list(lst):
    result=reduce(lambda x,y:x*y,lst)
    return result
nums=[1,2,3,4,5]
result=multiply_list(nums)
print(result)