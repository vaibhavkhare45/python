class animal:
    @staticmethod
    def run():
        print("run")
    
    @staticmethod
    def walk():
        print("walk")
    
    @staticmethod
    def swim():
        print("swim")

class dog(animal):

    def __init__(self,color):
        self.color = color

class cat(dog):

    def __init__(self,eat):
        self.eat = eat

ani = cat("Eat food")
print(ani.eat)
print(ani.run())