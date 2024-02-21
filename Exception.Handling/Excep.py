try:
  num = int(input("Enter a number :- "))
  for i in range(1,11):
    print(f"{num} x {i} = {i*num}")
except:
   print("Invalid Input!")
finally:
   print("Program End")