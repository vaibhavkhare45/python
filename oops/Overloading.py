class OverloadExample:
    def method(self, x):
        print("One argument method:", x)

    def method(self, x, y):
        print("Two arguments method:", x, y)

    def method(self, x, y, z):
        print("Three arguments method:", x, y, z)

# The last defined method with the name 'method' will be used
obj = OverloadExample()
obj.method(1)                 # This will raise a TypeError since no method with 1 parameter is defined
obj.method(1, 2)              # This will raise a TypeError since no method with 2 parameters is defined
obj.method(1, 2, 3)           # This will print "Three arguments method: 1 2 3"