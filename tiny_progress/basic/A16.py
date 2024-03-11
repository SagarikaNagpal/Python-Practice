# Question A16: WAP to input marks of a student and print the result (pass/fail) using conditional operator.


def passOrFail(a,b,c):
    name = input("name: ")
    print(a + b + c)
    if a+ b+c > 33:
        print("Pass")
    elif a+ b+c == 33:
        print("Reappear")
    else:
        print('Fail')

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
passOrFail(a,b,c)

