#a generator that generates the squares of numbers up to some number n
class MyNumbers:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return SquaresIterator(self.n)
class SquaresIterator:
    def __init__(self,n):
        self.n=n
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            result=self.current**2
            self.current+=1
            return result
        else:
            raise StopIteration
n=int(input())
my_numbers=MyNumbers(n)
my_iter=iter(my_numbers)
for x in my_iter:
    print(x)