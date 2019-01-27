# to count the number of words and number of characters in a given line of text except the spaces.


s = input("sentence is : ")
count = 0
for partition in s.split(" "):
    count += 1
print(count)


#for word

# for char
word = input("word: ")
a = [x for x in word]
print(a)


