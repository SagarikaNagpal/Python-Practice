# Question B40: WAP to input 2 numbers and find out the sum of all the even numbers
# which are not divisible by 5 but divisible by 3 and lies between the given two numbers.

def number():

    start = int(input('Starting digit = '))
    end = int(input('Ending digit = '))

    a = [i for i in range(start+1,end) if i%2 ==0 and i % 5 != 0 and i%3 ==0]
    a_sum = sum(a)
    print(f'numbers beween the range is : {a}')
    print(f'Sum is : {a_sum}')


number()


