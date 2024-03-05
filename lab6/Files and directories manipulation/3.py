#Write a Python program to test whether a given path exists or not.
#If the path exist find the filename and directory portion of the given path.
import os

path="C:\\Users\\Администратор\\pp2"
existence=os.access(path,os.F_OK)
if(existence):
    name=os.path.basename(path)
    directory=os.path.dirname(path)
    print("name:",name,"\ndirectory:",directory)
else:
    print("do not exist")