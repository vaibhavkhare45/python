"""7.Write a program to find average of numbers entered by the user."""
num = []
num1 = int(input("Enter Number :"))
num2 = int(input("Enter Number :"))
num3 = int(input("Enter Number :"))
num4 = int(input("Enter Number :"))
num5 = int(input("Enter Number :"))

num.append(num1)
num.append(num2)
num.append(num3)
num.append(num4)
num.append(num5)

total= sum(num)
print("Average of Number is ", total/len(num))
