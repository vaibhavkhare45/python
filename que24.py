"""Write a class calculator capable of 
finding square ,cube and square-root of a 
number."""


import math 
class calculator:

    def square(number):
        return number ** 2
    
    def cube(number):
        return number ** 3
    
    def square_root(number):
        return math.sqrt(number)


print(calculator.square(5))
print(calculator.cube(6))
print(calculator.square_root(16))