#Write a Python program to check for access to a specified path.
#Test the existence,readability,writability and executability of the specified path
import os

path="C:\\Users\\Администратор\\pp2"

exists = os.access(path, os.F_OK)
print(exists)

readable = os.access(path, os.R_OK)
print(readable)

writable = os.access(path, os.W_OK)
print(writable)

executable = os.access(path, os.X_OK)
print(executable)