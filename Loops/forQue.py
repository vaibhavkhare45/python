#1.

# list = [1,4,9,16,36,49,64,81,100]
# for el in list:
#     print(el)

#2.

tuple = (1,4,9,16,36,49,64,81,100)
user = int(input("Which num you find :"))
for el in tuple:
    print(el)
    if (user ==el):
        print("Found",el)
    else:
        print("NOT FOUND")
