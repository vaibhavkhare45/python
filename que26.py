"""WAP to find whether a number is prime 
or not using a while loop."""

# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:

num = int(input("Number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is  a prime number")
        break
    