def Odd():
    l = []
    low = int(input('Write smaller Number: '))
    higher = int(input('Write higher Number: '))

    if low>higher:
        print('Smaller should be lower than higher')
        return False
    else:
        for i in range(low,higher+1):
            if i %2 != 0:
                l.append(i)
        return l

def main():
    first =  Odd()
    print("list: ",first )
if __name__ == '__main__':
    main()






