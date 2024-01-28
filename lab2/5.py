#python sets
#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#class <set>
myset = {"apple", "banana", "cherry"}
print(type(myset))
#set constructor
thisset = set(("apple", "banana", "cherry")) #double round-brackets
print(thisset)
#access set items
#1ex
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#2ex
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#add set items
#1ex
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#2ex
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#remove set items(clear,del,discard,remove)
#1ex
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#sets are unordered, so when using the pop() method, you do not know which item that gets removed.
#loop sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)