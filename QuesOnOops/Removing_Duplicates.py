# Question: Complete the script so that it removes duplicate items from list a .
#
# a = ["1", 1, "1", 2]-- "1 is duplicate here"
# Expected output:
#
#   ['1', 2, 1]

# ********************Diifferent Approach***********************

# a = ["1",1,"1",2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(list(set(a)))

# ********************Diifferent Approach***********************

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)


