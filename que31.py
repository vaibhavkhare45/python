"""WAP to find out whether a file is 
identical and matches the context of another 
file."""


import os

try:
    file1 = "test.txt"
    file2 = "test2.txt"

    with open(file1, 'r') as f1:
        data1 = f1.read()
        
    with open(file2, 'r') as f2:
        data2 = f2.read()

    if data1 == data2:
        print("The files are identical and have the same content.")
    else:
        print("Both files are different")
        
except FileNotFoundError:
        print("One or both files not found.")
except IOError:
        print("Error reading files.")