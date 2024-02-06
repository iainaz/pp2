def has_333(nums):
    for x in range(len(nums)-1):
        if nums[x]==3 and nums[x+1]==3:
            return True
    return False
n=input()
n_list=[int(x) for x in n.split()]
if has_333(n_list):
    print("true")
else:
    print("false")