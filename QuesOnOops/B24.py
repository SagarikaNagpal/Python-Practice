# Question B24: WAP to input two numbers and a choice and calculate the result according to the following conditions:
# 		Choice						Result
# 1	Add
# 2	Subtract
# 3	Multiply
# 4	Divide
# 5	Remainder

n1 = int(input("1st : "))
n2 = int(input("2nd: "))
choice = int(input("choice"))
if(choice==1):
    print(n1+n2,"Adding")
elif (choice == 2):
    print(n2-n1, "subtracting")
elif(choice == 3):
    print(n1 * n2, "multiplying")
elif (choice == 4):
        print(n2 %n1, "reminder")
