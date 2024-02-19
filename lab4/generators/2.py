#write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console
class MyNumbers:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return SquaresIterator(self.n)
class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            result=self.current
            self.current+=2
            return result
        else:
            raise StopIteration
n = int(input())
my_numbers = MyNumbers(n)
my_iter = iter(my_numbers)
result=",".join(map(str,my_iter))
print(result)