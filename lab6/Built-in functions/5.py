#Write a Python program with builtin function that returns True if all elements of the tuple are true
def truetuple(tuplle):
    return all(tuplle)
tuples = [
    (True, True, True),
    (True, False, True),
    (),
    (1, 2, 3),
    (0, 1, 2),
    ('a', 'b', ''),
]

for tuple_i in tuples:
    print(f"{tuple_i}: {truetuple(tuple_i)}")