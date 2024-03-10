""""Create a class programmer for storing 
information of a few programmers working at 
microsoft."""


class programmer:
    def __init__(self, name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch

p1 = programmer("vaibhav",20,"web-developer")
print(p1.name,p1.age,p1.branch)

p2 = programmer("ayush",19,"app-developer")
print(p2.name,p2.age,p2.branch)
