class Complex:

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def ShowNumber(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self, num2): #Dunder function Addition
        newReal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newReal,newimag)

num1 = Complex(1,3)
num1.ShowNumber()

num2 = Complex(4,5)
num2.ShowNumber()

num3 = num1+num2
num3.ShowNumber()