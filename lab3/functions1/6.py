def rev_str(string):
    words=string.split()
    rev=' '.join(reversed(words))
    print(rev)
n=input()
rev_str(n)