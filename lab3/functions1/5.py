from itertools import permutations
def p(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
n=input()
p(n)