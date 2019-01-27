# a function to search a given string into another string and returns the position if found otherwise returns 0.
# Both the strings are passed to the function as argument.


def strings(str,str2):
    str = "kya hua"

    q = str2 in str
    if(q== True):
        findin = str.find(str2)
        return findin

        count = str1.count(str2)
        return count

    else:
        return 0

str2 = input("type: ")
print(strings(str,str2))
