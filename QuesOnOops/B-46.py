# WAP to input a number and count its even and odd digits and find out their sum separately.

def countEvenOdd(n):
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("\nOdd count : ", odd_count)
    if (even_count % 2 == 0 and
            odd_count % 2 != 0):
        return 1
    else:
        return 0


# Drive code
n = int(input("n: "))
t = countEvenOdd(n);

if (t == 1):
    print("YES")
else:
    print("NO")