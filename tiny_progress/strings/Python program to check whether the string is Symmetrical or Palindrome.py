# Python program to check whether the string is Symmetrical or Palindrome

def symmetrical(a):
    half = int(len(a)/2)
    firstStr = a[half:]
    secStr = a[:half]
    if firstStr == secStr:
        print('String is Symmetrical')
    else:
        print("string is not sym")

def palindrome(a):
    if a == a[::-1]:
        print("String is palindrome")
    else:
        print("Not palindrome")

a = input("String is: ")

symmetrical(a)
palindrome(a)
