# Question B25: WAP to input two numbers and an operator and calculate the result according to the following conditions:
# 		Operator					Result
# ‘+’						Add
# ‘-‘						Subtract
# ‘*’						Multiply

n1= int(input("n1"))
n2 = int(input("n2"))
opr = input("choice")

if(opr== '+'):
    print(n1+n2)

elif(opr== '-'):
    print(n1-n2)

elif (opr == '*'):
    print(n1*n2)


