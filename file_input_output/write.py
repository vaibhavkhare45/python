f =open("demo.txt","w")
f.write("New line added") #overwrites the entire file

f = open("demo.txt","a")
f.write("\nThis is new line")#adds to the file
