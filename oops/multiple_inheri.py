class animal:
    @staticmethod
    def run():
        print("run")
    
    @staticmethod
    def walk():
        print("walk")
    
    @staticmethod
    def bark():
        print("bark")

class aquaAnimal:
    @staticmethod
    def eat():
        print("eat")
    
    @staticmethod
    def swim():
        print("swim")

class dog(animal,aquaAnimal):

    def __init__(self,color):
        self.color = color



ani = dog("Brown&black")
print(ani.color)
ani.eat()
ani.walk()