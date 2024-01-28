#booleans
#1ex
print(5 > 4)
print(5 == 4)
print(5 < 4)
#2ex
a=200
b=30

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3ex
print(bool("ainaz"))
print(bool(17))

#4ex
x = "ainaz"
y = 17

print(bool(x))
print(bool(y))
#5ex
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#6ex
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#7ex
class myclass():
  def __len__(self):
    return 0

moshi = myclass()
print(bool(moshi))
#8ex
def myFunction() :
  return True

print(myFunction())
#9ex
def ainaz() :
  return True

if ainaz():
  print("yes!")
else:
  print("no!")
#10ex
x = 200
print(isinstance(x, int))