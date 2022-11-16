import math 
print("please insert operator :")
op=input()

if op=="+" or op=="-" or op=="/" or op=="*":
 a=float(input("please insert first number: "))
 b=float(input("please insert second number: "))
else:
     a=float(input("please insert number: "))
if op=="+":
    result=a+b
elif op=="-":
    result=a-b
elif op=="*":
    result=a*b
elif op=="/":
    if b==0:
       result="Division by zero is not possible"
    else:
        result=a/b
elif op=="sin":
    a=a*math.pi/180
    result=math.sin(a)
elif op=="cos":
    a=a*math.pi/180
    result=math.cos(a)
elif op=="tan":
    a=a*math.pi/180
    result=math.tan(a)
elif op=="cot":
    a=a*math.pi/180
    result=math.comb(a)                
elif op=="log":
    result=math.log(a)     
elif op=="sqrt":
    result=math.sqrt(a)
elif op=="factorial":
    result=math.factorial(a)             
    
print(result)    


