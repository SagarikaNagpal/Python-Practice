name = input("name of an employee: ")
salary = int(input("input of salary: "))

HRA = 0

DA = 0

if(salary> 5000 and salary <10000):

  print("Salary is in between 5000 and 10000")

  HRA = salary *0.1

  DA = salary * 0.05

elif(salary>10001 and salary<15000):

    print("Salary is in between 10001 and 15000")

    HRA = salary * 0.15

    DA = salary * 0.08

print(name)
print(salary)
print(HRA)
print(DA)






