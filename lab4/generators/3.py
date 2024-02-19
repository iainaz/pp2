#define a function with a generator which can iterate the numbers,which are divisible by 3 and 4,between a given range 0 and n
class d:
    def __init__(self,n):
        self.n = n
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1
        while self.current <= self.n:
            if self.current % 3 == 0 and self.current % 4 == 0:
                return self.current
            self.current += 1
        raise StopIteration
n = int(input())
my_numbers=d(n)
for x in my_numbers:
    print(x)