# https://www.geeksforgeeks.org/python-program-for-compound-interest/

# A = P(1 + R/100) t
# Compound Interest = A – P

def compoundInterest(p,r,t):
    a = p* pow((1+r/100),t)
    c1= a-p
    return c1

print(compoundInterest(10000, 10.25, 5))