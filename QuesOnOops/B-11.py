# Question B11: WAP to input monthly salary from the user and calculate the income tax according to the following rules:
# 		Salary				income tax
# 		>=9000			40% of the salary
# 		7500-8999			30% of the salary
# 		<7500				20% of the salary
salary = int(input("provide salary: "))
incmtax= 0
if(salary>=9000):
  print("after owning Rs 9000")
  salary=salary*0.4
  print("the amount will be in hand: ",salary)

elif(salary<=7500 and salary>=8999):
    print("salary from 7500 to 8999: ")
    salary=salary*0.3
    print("amount will be in hand" ,salary)

elif(salary<7500):
    print("after ownening less than Rs 7500")
    salary=salary*0.2
    print("amount will bee in hand: ",salary)


