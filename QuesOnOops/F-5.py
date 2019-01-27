# Write a function that has three arguments principle, rate and time and returns the simple interest.

def income(p,r,t):
    income = (p*r*t)/100
    return income

p = int(input("principal= "))
r = int(input("rate= "))
t = int(input("time= "))

print(income(p,r,t))