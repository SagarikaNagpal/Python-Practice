#create a dict of key a,b,c where each key has a value from 1 to 10 ,11 to 20 and 21 to 30
# expected output: {'a':[1,2,3,4,5,6,7,8,9,10],
#                   'b':[11...........20],
#                   'c': 21.........30]}
#
d = dict(a = list(range(1,11)),b =(list(range(11,21))),c =list(range(21,31)))
for key, value in d.items():
    print(d)


# if [d] == {'a'}:
#     print(list(range(1,11)))
#
# if [d]=={'b'}:
#     print(list(range(11,21)))
#
# if [d] == {'a'}:
#     print(list(range(21,30)))




# ******************************************************

# my_dict = dict()
#
# user_input = input("Enter key and value separated by commas (,): ")
#
# key, value = user_input.split(",")
#
# # // key = key.strip()
# # // value = value.strip()
#
# my_dict[key] = value
#
# print(my_dict)

# *********************************************************

# my_dict = dict()
#
# key = input("Enter the key: ")
# value = input("Enter the value: ")
#
# my_dict[key] = value
# print(my_dict)