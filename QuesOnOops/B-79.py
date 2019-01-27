#palindrome in int
n = int(input("Enter number: "))
rev = 0
while (n > 0):
     n = n // 10
     print(n)
if(n==n[::-1]):
    print("is palindrome!")
else:
    print("nope not palindrome")
