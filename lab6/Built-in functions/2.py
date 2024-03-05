#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case(s):
    ucc, lcc = 0, 0
    for char in s:
        if char.isupper():
            ucc += 1
        elif char.islower():
            lcc += 1
    return ucc, lcc

# Example string
input_string = "Hello mIr!"
upper_count, lower_count = count_case(input_string)
print(f"Number of Upper case letters:{upper_count}")
print(f"Number of Lower case letters:{lower_count}")