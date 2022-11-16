import math
a=float(input("please insert first side"))
b=float(input("please insert second side"))
c=float(input("pleae insert third side"))

if c>a+b or a>b+c or b>c+a:
    print("It is NOT! possible to draw this triangle")
else :print("It is possible to draw this triangle")    



