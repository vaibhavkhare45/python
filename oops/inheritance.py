class animal:
    @staticmethod
    def run():
        print("run")
    
    @staticmethod
    def bark():
        print("bark")
    
    @staticmethod
    def swim():
        print("swim")

class dog(animal):

    def __init__(self,color):
        self.color = color

ani= dog("Brown&black")
print(ani.color)
print(ani.swim())