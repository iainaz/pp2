#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:", directories)

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Files:", files)

    all_dirs_files = os.listdir(path)
    print("All Directories and Files:", all_dirs_files)

path='C:\\Users\\Администратор\\pp2'
list_directories_files(path)