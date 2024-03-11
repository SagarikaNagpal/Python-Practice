# Question A13: WAP to find out the quotient and remainder of two numbers. (Without using modulus ( % )  operator)


def quotient_and_remainder(divident, divisor):
    quotient = divident // divisor
    remainder = divident - divisor * quotient
    print(f'quotient : {quotient} , and remainder is {remainder}')
divident, divisor = int(input('divident: ')) , int(input('divisor: '))
quotient_and_remainder(divident, divisor)