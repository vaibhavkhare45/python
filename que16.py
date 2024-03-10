""". Create an empty dict. and allow five friends 
to enter their favourite language and use keys 
as their names Assume that the names are 
unique"""

dict={}
for i in range(1,6):
    name = input("Enter the Friends name: ")
    language = input("Enter the favourite: ")
    dict[name] = language

print(dict)