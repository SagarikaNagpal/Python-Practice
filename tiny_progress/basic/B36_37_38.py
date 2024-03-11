# Question B36: WAP to print the sum and average of first n natural numbers.
# Question B37: WAP to print the sum and average of first n odd numbers.
# Question B38: WAP to print the sum and average of first n even numbers.

criteria = int(input('Press 1 for sum of all natural number, 2 for even , 3 for odd , 4 for all  '))
if criteria>4:
    print('Number not valid!!')
n = int(input('What the range of the numbers would be? '))
def Numbers():
    if criteria == 1:
        a = [i for i in range(1,n+1)]
        print(a)
        a_sum = sum(a)
        print(f'Sum of natural number is: {a_sum}')
        a_average = a_sum/n
        print(f'Average of natural num is: {a_average}')

    elif criteria == 2:
        b = [i for i in range(1,n+1) if i%2 ==0]
        print(b)
        b_sum = sum(b)
        print(f'Sum of Even number is: {b_sum}')
        b_average = b_sum/n
        print(f'Average of Odd num is: {b_average}')

    elif criteria == 3:

        c = [i for i in range(1, n + 1) if i % 2 != 0]
        print(c)
        c_sum = sum(c)
        print(f'Sum of Even number is: {c_sum}')
        c_average = c_sum / n
        print(f'Average of Odd num is: {c_average}')

    elif criteria == 4:
        a = [i for i in range(1, n + 1)]
        a_sum = sum(a)
        print(f'Sum of natural number is: {a_sum}')
        a_average = a_sum / n
        print(f'Average of natural num is: {a_average}')

        b = [i for i in range(1, n + 1) if i % 2 == 0]
        b_sum = sum(b)
        print(f'Sum of Even number is: {b_sum}')
        b_average = b_sum / n
        print(f'Average of Odd num is: {b_average}')

        c = [i for i in range(1, n + 1) if i % 2 != 0]
        c_sum = sum(c)
        print(f'Sum of Even number is: {c_sum}')
        c_average = c_sum / n
        print(f'Average of Odd num is: {c_average}')


Numbers()
