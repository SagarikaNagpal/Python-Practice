# Question B78: Write a menu driven program which has following options:
# 1.	Factorial of a number.
# 2.	Prime or Not
# 3.	Odd or even
# 4.	Exit.

n = int(input('Number is : '))
choice = int(input('Choices are: '))
def options():
    if choice == 1:
        factorial_list = []
        factorial = 1
        for i in range(1,n+1):
            factorial *= i
            factorial_list.append(factorial)
        print(factorial_list)

    if choice == 2:
        divisibleBy = []
        if n == 1:
            print('Number should be greater than 1')
        else:
            for i in range(2,n+1):
                if n % i == 0:
                    divisibleBy.append(i)

        if divisibleBy:
            print(f'It is not a prime number as the number is divisible by {divisibleBy}')
        else:
            print('It is a prime number')

    if choice == 3:
        if n % 2 == 0:
         print(f'Number is Even!')
        else:
            print(f'Number is odd!')

    if choice ==4:
        print('It will exit the processing!!!!')
        exit()
options()
