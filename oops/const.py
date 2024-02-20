class Student():

    #default constructors
    def __init__(self):
       pass
    
    #parameterized constructors
    def __init__(self,name,marks):
     self.name= name
     self.marks=marks
     print("Adding new student in database..")

s1 = Student("Vaibhav khare",98)
print(s1.name,s1.marks)

s2 = Student("Ayush Rai",89)
print(s2.name,s2.marks)