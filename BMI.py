import math
print("BODY MASS INDEX")
w=float(input("please insert your weight (KG): "))
h=float(input("please insert your height (meter)"))
b=w/(h*h)
print ("Your BMI :",b)
if b<18.5:
    print("Underweight")
elif 18.5<b<24.9:
    print("Underweight")
elif 25<b<29.9:
    print("Overweight")    
elif 30<b<34.9:
    print("Obeslty") 
elif 35<b<39.9:
    print("Extreme Obeslty")    