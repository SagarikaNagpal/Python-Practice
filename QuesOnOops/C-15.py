# to check a string for palindrome.
# also work with b-79
# String="aIbohPhoBiA"
# String1=String.casefold()
# Rev_String=reversed(String1)
# if(list(String1)==list(Rev_String)):
#     print("The string is palindrome")
# else:
#     print("no its not")


s= input("string: ")
s1 = s.casefold()
print(s1)
rev = reversed(s)
print("rev",rev)

if(list(s1)==list(rev)):
    print("string is palindrome")

else:
    print("no its not")
