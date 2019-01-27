
r=int(input("radius: "))
a=int(input("Ist num: "))
b=int(input("IInd num: "))
area=3.14*r*r
add=a+b
mul=a*b
input=int(input("choice is: "))
if(input==1):
    print("Area of circle: ",area)
elif(input==2):
    print("addition is: ",add)
elif(input==3):
    print("multiplication is: ",mul)
else:
    print("thanks!")