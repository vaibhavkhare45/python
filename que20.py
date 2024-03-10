"""Write a program whether the user 
name contain less than 10 character or not"""

user = input("Enter your name: ")
print(len(user))
if len(user) < 10:
    print("Taken less than 10 characters")
else:
    print("Taken more than 10 characters")