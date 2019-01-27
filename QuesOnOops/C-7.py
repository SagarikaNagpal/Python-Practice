# # WAP to search a character in a given string.

s = "tell me one thing"

ch = input("press ur word for searching: ")

word = ch in s

if(word==True):
    position = s.index(ch)
    indexing = s.find(ch)
    print(position,"is position")
    print(indexing,"is indexing")   # indexing and position arelmost doing same thing!
else:
    print ("no wrd is here")