# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}
#
# # printing original dictionary
# print("The original dictionary is : " + str(test_dict))
#
# # Extract Unique values dictionary values
# # Using set comprehension + values() + sorted()
# res = list(sorted({ele for val in test_dict.values() for ele in val}))
#
# # printing result
# print("The unique values list is : " + str(res))

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

print(f'Original dict: {test_dict}')

unique_dict = list(sorted({ele for val in test_dict.values() for ele in val}))
print(f'Unique_dict {unique_dict}')