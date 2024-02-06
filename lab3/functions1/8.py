def spy_game(nums):
    for x in range(len(nums)):
        if nums[x]==0 and nums[x+1]==0 and nums[x+2]==7:
            return True
    return False
n=input()
n_list=[int(x) for x in n.split()]
if spy_game(n_list):
    print("true")
else:
    print("false")