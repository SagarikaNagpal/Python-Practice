# Question C6: WAP to count the lower case and upper case letters in a string.

def counting():
    i = input('Word is : ')
    lower_count = 0
    upper_count = 0
    for char in i:
        if char.islower():
            lower_count +=1
        elif char.isupper():
            upper_count += 1
    print(f'Small cases are: {lower_count}')
    print(f'Upper cases are: {upper_count}')
counting()
