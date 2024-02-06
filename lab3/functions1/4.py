def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def filter_prime(nums):
    return[num for num in nums if is_prime(num)]
numbers=[2,3,5,7,11,13,17,50]
result=filter_prime(numbers)
print(result)