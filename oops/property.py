class Student:
    def __init__(self,phy,chem,math):   
        self.phy =phy
        self.chem =chem
        self.math =math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+ "%"

sub = Student(47,56,72)
print(sub.percentage)