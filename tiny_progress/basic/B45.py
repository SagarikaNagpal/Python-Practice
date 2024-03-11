# Question B45: WAP to check that given number is prime or not.

def primeNum():
    num = int(input('Number is: '))
    if num == 1:
        print('Print natural number greater than 1')
    else:
        divisor = []
        for i in range(2, num):
            if num % i == 0:
                print(i)
                divisor.append(i)
        if divisor:
            print(f'Not Prime because {divisor} can divide {num}')
        else:
            print('Prime')

primeNum()