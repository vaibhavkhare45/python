class Student:

    def __init__(self,name,marks):
       self.name = name
       self.marks = marks

    def welcome(self): #method
      print("Welcome My friend", self.name)

s1 = Student("vaibhav",98)
s1.welcome()
print(s1.welcome)