"""WAP to print a multiplication table for a 
given number using a for loop."""

num = int(input("Number of multiplication: "))

for i in range(1,11):
    print(f"{num} x {i} = {i*num}")
    