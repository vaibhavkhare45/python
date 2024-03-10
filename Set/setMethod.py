# SET METHODS

marks = set()
marks.add(1) #add element
marks.add(2)
marks.add(3)
marks.add(4)
print(marks)
marks.remove(4)#remove element

marks.clear()#empty elment

print(marks)

collection = {"hello","vaibhav", "coding", "python"}
print(collection.pop()) #remove random value

set1 = {1,2,3,5,6}
set2 = {3,2,1,4,5,6}
print(set1.union(set2)) #combines two sets

print(set1.intersection(set2))