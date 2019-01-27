n1 = int(input("num1: "))
n2 = int(input("num2: "))
choice = (input("choice is :"))

if(choice=='+'):
    print((n1+n2)," is the adding")

elif(choice=='-'):
    print((n2-n1) ," is the sub")

elif(choice=='*'):
    print((n1*n2),"is multip")

elif(choice=='/'):
    print((n2/n1),"is div")

elif(choice=='%'):
    print((n2%n1),"is mod")

else:
    print("out of range")