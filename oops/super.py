class animal:
  
  def __init__(self,type):
    self.type = type

    @staticmethod
    def bark():
        print("bark")
    
    @staticmethod
    def swim():
        print("swim")

class dog(animal):

    def __init__(self,color):
        self.color = color
        super().__init__(type)
        super().swim()
        

s1 = dog("black")
print(s1.type)