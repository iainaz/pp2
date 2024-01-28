#lists
#1ex
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2ex
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3ex
list1 = ["abc", 34, True, 40, "male"]
#4ex
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#access list
#1ex
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#2ex
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#3ex
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#change list items
#1ex
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#2ex
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#add list items
#1ex
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#2ex
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#3ex
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#remove list items
#1ex
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#2ex
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#3ex
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#4ex
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#5ex
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#loop lists
#1ex
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#2ex
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#3ex
thislist=["a","b","c"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1
#4ex
[print(x) for x in thislist]
#list comprehension
#1ex
fruits=["alma","banan","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
#2ex
fruits=["alma","banan","mango"]
newlist=[x for x in fruits if "a" in x
#3ex
newlist = [x for x in range(10)]
print(newlist)]
#sort lists
#1ex
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#2ex
thislist.sort(reverse = True)
print(thislist)
#3ex
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#4ex
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)