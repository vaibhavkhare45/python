class Student:
    collage_name = "ABC Collage" #class attribute 

    def __init__(self,name,age):
        self.name = name #object attribute
        self.age = age
        print("Adding new Student in Database")

S1 = Student("vaibhav",20)
print(S1.name,S1.age)
print(Student.collage_name)

