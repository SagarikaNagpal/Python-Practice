# Question B80: WAP to input a number and find out the sum of its digits.

def sumOfDigits():
    n = int(input('Digits: '))
    sum_digits = 0
    for i in str(n):
        digit = int(i)
        sum_digits += digit
    print(sum_digits)
sumOfDigits()
