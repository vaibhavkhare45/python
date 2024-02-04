name = input("Enter Your Name :")
sub1 = float(input("Subject Number :"))
sub2 = float(input("Subject Number :"))
sub3 = float(input("Subject Number :"))

if sub1>= 33:
      if sub2>= 33:
           if sub3 >= 33:
            percentage =(((sub1+sub2+sub3)/300)*100)
               if percentage >=40:
                     print("Pass")
               else:
                 print("Fail")
             else:
       print("Fail")
else:
    print("Fail")
else:
print("Fail")

