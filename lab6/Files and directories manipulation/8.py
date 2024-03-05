#Write a Python program to delete file by specified path.Before deleting check for access and whether a given path exists or not.
import os
path='path'
existence=os.access(path,os.F_OK)
if existence:
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        os.remove(os.path.join(path,file))
else:
    print('path do not exist')