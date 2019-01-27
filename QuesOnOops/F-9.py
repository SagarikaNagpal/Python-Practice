# : Write a function that has one character argument and displays that it’s a small letter, capital letter, a digit or a special symbol.
#                                                                              97-122        65-90             48-57             33-47
def ch(a):
    if(a.isupper()):
        print("upper letter")
    elif(a.islower()):
        print("lower letter")
    elif (a.isdigit()):
        print("is digit")
    else:
        print("Special")


a=input("ch is: ")
print(ch(a))