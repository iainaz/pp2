#Write a Python program to write a list to a file.
mylist=['file','file1','file2']
with open('file.txt','w')as file:
    for i in mylist:
        file.write(i+'\n')