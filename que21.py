"""Write a program to calculate the grade of his 
marks from the following scheme.
90 – 100 = O grade
80 – 90 = E grade
70 – 80 = A grade
60 – 70 = B grade
50 – 60 = C grade
Below 50 is fail"""


marks = float(input("Enter Your marks: "))

if marks >= 90:
    print("O grade")
elif marks >= 80:
    print("E grade")
elif marks >= 70:
    print("A grade")
elif marks >= 60:
    print("B grade")
elif marks >= 50:
    print("C grade")
else:
    print("Fail")

print("Your grade: ", marks)