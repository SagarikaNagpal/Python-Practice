# Question A23: WAP to input employee code, name and basic salary of an employee and calculate the following values:
# 		HRA					40 % of basic salary
# 		DA					10 % of basic salary
# 		CCA					5 % of basic salary
# 		GS					Basic + HRA + DA + CCA
# 		PF					10 % of GS
# 		IT					10 % of GS
# 		NS					GS – (PF + IT)
# Display all the values.

code = int(input("code is: "))
name = (input("name is: "))
salary = int(input("salary: "))
HRA = (0.40* salary)
DA = (0.10 * salary)
CCA = (0.05* salary)
GS = salary+ HRA+DA+CCA
PF = 0.1*GS
IT = 0.1*GS
NS = GS-(PF+IT)
print(name)
print(salary)
print(HRA)
print(DA)
print(CCA)
print(GS)
print(PF)
print(IT)
print(NS)



