"""Write a program to fill in a letter 
template given below with name & date.
Letter = “Dear < NAME>
Welcome to CSIT
<DATE>’”
"""

name  = input("Enter your name: ")
date = int(input("Enter todays date: "))

print(f"Dear, {name}\nWelcome to CSIT\n {date}")