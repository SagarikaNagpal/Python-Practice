# Write a function to search a string in the array of strings. String and array of strings should be passed to the function as parameters.


def searching(list,arr):
    list = "hey , wtsup"
    arr = []

    if(arr in list==True):

        finding=list.find(arr)
        return finding

arr=[input("arr is: ")]

print(searching(arr,list))

# def calve(list,st):
#     list=["sahil","nikki"]
#     if(st in list):
#         return "True"
#     else:
#         return "False"
#
# print(calve("","kimmy"))

