# Question B2: WAP to input the age of a person and check that he is eligible for license for not.

def age(n):
    if n > 18:
        print('Yes you are eligible')
    else:
        print('You have be be elder than 18')

n = int(input('N:'))
age(n)
