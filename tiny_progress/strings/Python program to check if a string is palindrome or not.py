def palindrome(a):
    if a == a[::-1]:
        print('True')
    else:
        print('False')

a = input('Check the string: ')
palindrome(a)