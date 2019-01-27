# Question B13:input a character and check that it’s a small letter, capital letter, a digit or a special symbol.

ch= input("to check what is it?: ")
if(ch.islower()):
    print("ch is a lower")

elif(ch.isupper()):
    print("ch is upper")

if(ch.isdigit()):
    print("ch is a digit")

else:
    print("is a spcl symbol")






