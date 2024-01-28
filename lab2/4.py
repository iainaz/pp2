#tuples
#1ex
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#access tuple
thistuple = ("aaa", "bbb", "ccc")
print(thistuple[1])
#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#unpack tuples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#loop tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#join tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)