# WAP to search a given string into another string and displays the position if found otherwise displays 0

s = "ye dil mange more"

a = input("another string: ")

w = a in s

if(w==True):
    finding = s.find(a)
    print("finding place from zero=",finding)
    counting = s.count(a)
    print(counting,"=counting  states  for how many times it come")

else:
    print(0)

