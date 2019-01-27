# Write a function that returns 1 if the number is prime and 0 if not prime.
# Number is passed to the function as argument.

# def prime(a):
#     n = 1
#     if (n>1):
#         for i in range(2,n):
#             if(n % i )==0:
#                 return 1
#
#             else:
#                 print("num is not prime")
#
#                 return 0
#
# print(prime(7))


def prime(n):
    if(n>1):

        for i in range(2,n):
            if(n%i)==0:
                #print("num is not prime")
                return 0
                break
            else:
                #print("num is prime")
                return 1
                break

n =int(input("num is: "))
print(prime(n))

