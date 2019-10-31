# Question: Please complete the script so that it prints out a list slice containing items d , e , and f .
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:
# ['d', 'e', 'f']
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6],"for d e f")
print(letters[:3],"for a b c ")
print(letters[-2],"for i")
print(letters[-3:],"for 'h', 'i', 'j'")
print(letters[0::2],"for 'a', 'c', 'e', 'g', 'i' ")
