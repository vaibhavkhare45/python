"""4.Write a program to print Contents of a a directory using
OS module. Search online for the function which does that"""

import os
directory = "C:\Users\USER\OneDrive\Desktop\javalab"
if not os.path.exists(directory):
    print("Directory is invalid")
else:
    for i in os.listdir(directory):
        print(i)
