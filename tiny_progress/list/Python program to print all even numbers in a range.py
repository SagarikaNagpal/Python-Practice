def listCreate():
    l = []
    start = int(input('Enter lower number, List starts from: '))
    stop = int(input('Enter higher number, List ends here: '))

    for i in range (start,stop+1):
        if i%2==0:
            l.append(i)
    return l

def main():
    first = listCreate()
    print("list: ",first )

if __name__ == '__main__':
    main()


