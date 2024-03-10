"""Write a program to input 8 numbers 
from the user and display all the unique 
numbers at once"""

numbers = [1,1,2,3,3,4,4,5,6,4,5,7,8]
unique_number=set(numbers)
print(list(unique_number))