# Question B8: WAP to input the salary of a person and calculate the hra and da according to the following conditions:
# 		Salary 				HRA		DA
#  		5000-10000			10%		5%
# 		10001-15000			15%		8%
name = str(input("name"))
sal = int(input("sal is: "))
HRA = 1
DA = 1

if((sal>5000 and sal< 1000)):

    HRA = (0.1*sal)
    DA = (0.5 *sal)


if((sal>10001 and sal <15000)):
    HRA = (1.5*sal)
    DA = (0.8*sal)

print()
print("HRA", HRA)
print("DA", DA)
