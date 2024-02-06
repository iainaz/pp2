def unique(nums):
    newset=[]
    for x in nums:
        if x not in newset:
            newset.append(x)
    return newset
n=input()
nlist=[int(x) for x in n.split()]
result=unique(nlist)
print(result)