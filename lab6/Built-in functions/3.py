#Write a Python program with builtin function that checks whether a passed string is palindrome or not
def ispalindrome(s):
    st=s.replace(" ","").lower()
    return st==st[::-1]
s=input()
if ispalindrome(s):
    print("palindrome")
else:
    print("not palindrome")