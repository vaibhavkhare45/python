"""Write a program to store 7 vegetables 
within a list enter by the user."""

list = []
for i in range(0,7):
    veg  = input("Enter vegetables name: ")
    list.append(veg)

print(list)