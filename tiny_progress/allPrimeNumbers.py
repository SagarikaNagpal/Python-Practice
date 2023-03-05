
# def prime(num):
#     if num >1 :
#         for i in range(2,num):
#             if(num%i ==0):
#                 print(num,'is not a prime number')
#                 break
#         else:
#             print(num,'Num is a prime number')
#     else:
#         print("Num is not a  prime numm")
# num = int(input("Num: "))
# print(prime(num))


## All prime numbers between the interval:
def primeNumber(l,u):
     for i in range(l,u+1):
         if i >1:
             for j in range(2, i):
                if i % j == 0:
                    break
             else:
                print('prime numbers are : ',i)

l = int(input("l: "))
u = int(input("u: "))
print(primeNumber(l,u))