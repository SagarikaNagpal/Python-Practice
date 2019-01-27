# WAP to find out the quotient and remainder of two numbers. ( Without using modulus ( % )  operator)

# div*quoti +rema = divi

num = int(input("num is:"))
divisor=  int(input("divisor is: "))
a = (num -divisor)*(num//divisor)

print(a)


# Number=int(input("Please enter the number"))
# Divisor=int(input("Please enter the divisor"))
#
# def getRemainder(num, divisor):
#     c=(num - divisor * (num // divisor))
#     print(c)
#     return c
#
#
#
#
#
# getRemainder(Number,Divisor)