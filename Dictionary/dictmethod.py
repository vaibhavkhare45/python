# DICTIONARY METHODS

myDict = {
        "name" : "Vaibhav",
        "age" : 20,
        "score":{
        "bio" : 98,
        "chem" : 97,
        "math" : 95
    }
}


print(myDict.keys()) #returns all keys

print(myDict.values()) #returns all values

print(myDict.items()) #returns all (key,value) pairs as tuple

print(myDict.get("key")) #reture the key according to value

myDict.update({"city" : "delhi"}) # inserts the specifiel item to the dictionary
print(myDict)