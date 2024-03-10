"""WAP to generate a multiplication table 
from 2 to 20 and
write it into different files and place their files in 
a folder for a 9 year old child.
"""
import os

folder_name = "tables"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for i in range (2,21):

    table =[f"{i} X {j} = {i*j}\n" for j in range (1,11)]
    
    file_name = (f"{folder_name}/table_{i}.txt")
    with open(file_name , "w") as file :
        file.writelines(table)
        
    
    

