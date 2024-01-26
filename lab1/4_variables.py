#ex1
x=5
y="ainaz"
print(x)
print(y)
#ex2
x = 4
x = "ainaz"
print(x)
#ex3
x=str(3)
y=int(3)
z=float(3)
#ex4
x=5
y="ainaz"
print(type(x))
print(type(y))
#ex5
x='ainaz'
y="ainaz"
#ex6
a=4
A="ainaz"
#variable names
myvar="ainaz"
my_var="ainaz"
_my_var="ainaz"
myVar="ainaz"
MYVAR="ainaz"
myvar2="ainaz"
#assign multiple values
x,y,z="alma","banan","shie"
print(x)
print(y)
print(z)

x=y=z="alma"
print(x)
print(y)
print(z)

fruits=["alma","banan","shie"]
x,y,z=fruits
print(x)
print(y)
print(z)
#output variables
x="ainaz is awesome"
print(x)

x="ainaz"
y="is"
z="awesome"
print(x,y,z)

x="ainaz "
y="is "
z="awesome"
print(x+y+z)

x=5
y=10
print(x+y)
#global variables
x="awesome"

def myfunc():
  print("ainaz is "+x)

myfunc()
#
x = "awesome"

def myfunc():
  x = "fantastic"
  print("ainaz is " + x)

myfunc()

print("ainaz is " + x)
#
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("ainaz is " + x)