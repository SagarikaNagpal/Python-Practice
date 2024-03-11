# Question B41: WAP to input the name and age of a person and print the name as many times as age.

def name():
    name = input('Name: ')
    age = int(input('Age: '))
    n = [print(name, end = ',' if i < age else '') for i in range (1,age+1) ]


name()

