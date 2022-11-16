import math
print("Calculation of the student's academic status")

firstname=input("please insert first name: ")
lastname=input("please insert last name: ")
a=float(input("please insert first number corse: "))
b=float(input("please insert second number corse: "))
c=float(input("please insert third number corse: "))
average=(a+b+c)/3
if average >= 17:
    print("Dear student: ",firstname,lastname,"Your educational status Is: GREATE")
elif 17>average >=12:
     print("Dear student: ",firstname,lastname,"Your educational status Is: NORMAL")
elif average <12:
     print("Dear student: ",firstname,lastname,"Your educational status Is: FAIL")     
