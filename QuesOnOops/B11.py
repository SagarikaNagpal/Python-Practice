# Question B11: WAP to input monthly salary from the user and calculate the income tax according to the following rules:
# 		Salary				income tax
# 		>=9000			40% of the salary
# 		7500-8999			30% of the salary
# 		<7500				20% of the salary

sal = int(input("sal : "))

if (sal >= 9000):
    sal = sal * 0.4
    print(sal)
elif (sal >= 7500 and sal <= 8999):
    sal = sal * 0.3
    print(sal, "of 7500")
else:
    sal = sal * 0.2
    print("sal lessthan 7500", sal)
