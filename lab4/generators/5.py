#implement a generator that returns all numbers from (n) down to 0
class MyNumbers:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return allnumbers(self.n)
class allnumbers:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        while self.n>=0:
            result=self.n
            self.n-=1
            return result
        raise StopIteration
n=int(input())
my_numbers=MyNumbers(n)
my_iter=iter(my_numbers)
for x in my_iter:
    print(x)