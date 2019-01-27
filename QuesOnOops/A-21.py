radius=int(input("rdius is: "))
area= 3.14*radius*radius
cir= 2*3.14*radius
user=int(input("put ur choice: "))
if(user==1):
    print("area is: ", area)
elif(user==2):
    print("circumfrence : ",cir)
else:
    print("no input requested")