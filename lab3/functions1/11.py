def polin(n):
    return n==n[::-1]
n=input()
if polin(n):
    print("this is polindrome")
else:
    print("not polindrome")