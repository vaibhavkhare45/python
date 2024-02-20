class Student:
    def __init__(self,name,rollno,Sem):
        self.name= name
        self.rollno = rollno
        self.Sem = Sem

S1 = Student("Vaibhav",50,3)
print(S1.name,S1.rollno,S1.Sem)