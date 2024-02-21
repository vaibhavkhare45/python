#initializes method

# class Magic:

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# m1 = Magic(4,5)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

point = Point(3, 4)
print(str(point)) 

