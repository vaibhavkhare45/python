""".WAP to read the text from a given file 
tortoise.txt to find out whether it contains the 
word “slow”"""

with open("tortoise.txt", 'r') as f:
     data = f.readlines()  
print(data)