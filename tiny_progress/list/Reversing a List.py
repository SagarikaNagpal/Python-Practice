def listCreate():
    l =[]
    n = int(input('num of items '))
    for i in range(n):
        l.append(int(input("place items: ")))
    return l

def listReverse(l):
    # l.reverse()
    list(reversed(l))
    return l
def main():
    firstProg = listCreate()
    print(f'List shown: {firstProg}')
    secondProg = listReverse(l=firstProg)
    print(f'Reversed List shown: {secondProg}')
if __name__ == '__main__':
    main()

#
# lst = [10, 11, 12, 13, 14, 15]
# lst.reverse()
# print()
# print("Using reverse() ", lst)
#
# print("Using reversed() ", list(reversed(lst)))
