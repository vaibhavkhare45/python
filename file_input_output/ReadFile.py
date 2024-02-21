#reading mode
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#Read Line

f = open("demo.txt","r")

line1 = f.readlines()
print(line1)

line2 = f.readlines()
print(line2)