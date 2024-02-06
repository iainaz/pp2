'''Write a program which can filter prime numbers in a list by using filter function.
Note: Use lambda to define anonymous functions.'''
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
numbers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
prime_nums=list(filter(lambda x:is_prime(x),numbers))
print(numbers)
print(prime_nums)