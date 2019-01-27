# Write a function to copy one string into another string. Both the strings are passed to the function as argument.

import copy
def st(str , str1):
    c = str
    c1 = str1.replace(str1,str)

    return c,c1

print(st("Sahil","Nagpal"))


