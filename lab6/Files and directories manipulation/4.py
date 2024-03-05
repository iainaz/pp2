#Write a Python program to count the number of lines in a text file.
with open('file.txt','r') as file:
    lines=file.readlines()
    num_of_lines=len(lines)
print(num_of_lines)