# Write a menu driven program which has following options:
# 1.	Factorial of a number.
# 2.	Prime or Not
# 3.	Odd or even
# 4.	Exit.

n = int(input("n: "))

menu = int(input("menu is: "))

factorial = 1


if(menu==1):
 for i in range(1,n+1):

    factorial= factorial*i

    print("factorial of ",n,"is",factorial)



elif(menu==2):

    if(n>1):

        for i in range (2,n):

            if(n%i)==0:

                print("num ",n,"is not prime")
                break
            else:

                print("num", n ,"is prime")
                break

    else:
        print("num is not prime")

elif(menu==3):

    if(n%2 ==0):

        print(n,"is even")

    else:

        print(n, "is odd")

else:
    print("exit!")
