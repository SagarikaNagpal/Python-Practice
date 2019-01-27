# to count the number of spaces, tabs and new line characters in a given string.
string = input("String is: ")
# ," ",'\t','\n')

space = 0
tabs  = 0
new_line = 0

for chara in string:
    if(chara == " "):
        space +=1

    elif(chara == '\t'):
        tabs += 1

    elif(chara== '\n'):
        new_line += 1


print("this is space",space)

print("this is tabs",tabs)

print("thos is new line",new_line)
