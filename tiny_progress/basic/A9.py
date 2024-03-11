# Question A9: WAP to input principle, rate and time from the user and
# calculate the simple interest and total amount. Display all the values.

'''Simple Interest = P×R×T / 100
P is the principal amount (the initial amount of money).
R is the rate of interest per time period.
T is the time duration (in years) for which the interest is applied.
'''


def simpleInterest(p,r,t):
    print(f'Simple interest of {p},{r},{t} is: ', (p*r*t)/100)
p = int(input('Princial'))
r = int(input('Rate'))
t = float(input('Time'))

simpleInterest(p,r,t)

