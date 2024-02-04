# DICTIONARY & SET
# info = {
#       "name" : "Vaibhav",
#        "Age" : 19,
#        "cgpa" : 9.6,
#        "Subject" : ["java","C", "Java"],
#        "topic" : ("dictionary", "Set"),
#        16 :54
# }
# # print(type(info))
# print(info["name"])
# print(info["Age"])

# # assgin new Values
# info["name"] = "vaibhav khare"
# info["Age"] = 20
# print(info)

# NESTED DICTIONARY*******
# student = {
#     "name" : "Vaibhav",
#     "age" : 20,
#     "score":{
#         "bio" : 98,
#         "chem" : 97,
#         "math" : 95
#     }
# }
# print(student["score"])

# DICTIONARY METHODS

# myDict = {
#         "name" : "Vaibhav",
#         "age" : 20,
#         "score":{
#         "bio" : 98,
#         "chem" : 97,
#         "math" : 95
#     }
# }


# print(myDict.keys()) #returns all keys

# print(myDict.values()) #returns all values

# print(myDict.items()) #returns all (key,value) pairs as tuple

# print(myDict.get("key")) #reture the key according to value

# myDict.update({"city" : "delhi"}) # inserts the specifiel item to the dictionary
# print(myDict)

# SETS IN PYTHON*******

# collection  = {1,2,3,4,"vaibhav","hellop",5}
# print(collection)
# print(type(collection))

# NULL SETS
# name = set() #empty set; syntax

# SET METHODS

# marks = set()
# marks.add(1) #add element
# marks.add(2)
# marks.add(3)
# marks.add(4)

# marks.remove(4)#remove element

# marks.clear()#empty elment

# print(marks)

# collection = {"hello","vaibhav", "coding", "python"}
# print(collection.pop()) #remove random value

# set1 = {1,2,3,5,6}
# set2 = {3,2,1,4,5,6}
# print(set1.union(set2)) #combines two sets

# print(set1.intersection(set2))

# QUETIONS

# 1.
# dict= {
#     "table" : ["A piece of furniture","List of facts & figures"],
#     "cat" : "a small animal"

# }
# print(dict)

# 2
marks = {}
x = int(input("enter phy :"))
marks.update({"phy": x})

y = int(input("enter bio :"))
marks.update({"bio": y})

z = int(input("enter chem :"))
marks.update({"chem": z})

print(marks)
