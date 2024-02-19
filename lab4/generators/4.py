#implement a generator called squares to yield the square of all numbers from (a) to (b)
#test it with a "for"loop and print each of the yielded values
class MyNumbers:
    def __init__(self, a, n):
        self.a = a
        self.n = n
    def __iter__(self):
        return squares(self.a,self.n)
class squares:
    def __init__(self, a, n):
        self.a=a
        self.n=n
        self.current=a
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            result=self.current ** 2
            self.current+=1
            return result
        else:
            raise StopIteration
a = int(input())
b = int(input())
my_numbers = MyNumbers(a, b)
for x in my_numbers:
    print(x)