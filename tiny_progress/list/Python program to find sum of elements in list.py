'''
    :param l:  User list
    :return: list
    '''
def createList():
    n = int(input('Number of elements in list: '))
    l = []
    for i in range(n):
        l.append(int(input('element is: ')))
    return l
def sumOfListNumbers(l):
    '''
    :param l:  User list
    :return: total -->sum of list elements in int data type
    '''
    total = 0
    for k in range(len(l)):
        total = total + l[k]
    return total

def main():
    firstProg = createList()
    print(f'List: {firstProg}')
    secProg = sumOfListNumbers(l=firstProg)
    print(f'Sum of List shown: {secProg}')
if __name__ == '__main__':
    main()