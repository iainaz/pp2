#if-else
#1ex   if
a = 33
b = 200
if b > a:
  print("b is greater than a")
#2ex   elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#3ex   else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#4ex   shortly
if a > b: print("a is greater than b")
#5ex   shortly
a = 2
b = 330
print("A") if a > b else print("B")
#6ex   and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#7ex   or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#8ex   not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#9ex
a = 33
b = 200

if b > a:
  pass