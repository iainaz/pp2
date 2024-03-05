#Write a Python program to copy the contents of a file to another file
source_file = 'file.txt'
destination_file = 'file1.txt'

with open(source_file, 'r') as src:
    with open(destination_file, 'w') as dst:
        contents = src.read()
        dst.write(contents)