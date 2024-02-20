class Account:

    def __init__(self,number,password):
        self.num = number
        self.__pass = password #this make password (__)private

    def reset(self): #but this time password was showing because we access inside the class
        print(self.__pass)

Acc1 = Account("1646987","njjdhd")
print(Acc1.num)
print(Acc1.reset())