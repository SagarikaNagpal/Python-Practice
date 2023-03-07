# Python program to swap two elements in a list
def appendList():
    user_lst = []
    no_of_items = int(input("How many numbers in a list: "))
    for i in range(no_of_items):
        user_lst.append(int(input("enter item: ")))

    return user_lst

def swapPos(swap_list):
    swap_index_1 = int(input("Enter First Index for swapping: "))
    swap_index_2 = int(input("Enter Second Index for swapping: "))
    swap_list[swap_index_1], swap_list[swap_index_2] = swap_list[swap_index_2], swap_list[swap_index_1]

    return swap_list


def main():
    saga_list = appendList()
    print("List Before Swapping: ", saga_list)
    print("List Sorted: ", sorted(saga_list))
    swapped_list = swapPos(swap_list=saga_list)
    print("List After Swapping: ", swapped_list)


if __name__ == '__main__':
    main()

