# Question A23: WAP to input employee code, name and basic salary of an employee and calculate the following values:
# 		HRA					40 % of basic salary
# 		DA					10 % of basic salary
# 		CCA					5 % of basic salary
# 		GS					Basic + HRA + DA + CCA
# 		PF					10 % of GS
# 		IT					10 % of GS
# 		NS					GS – (PF + IT)
# Display all the values

code = int (input("code : "))
name = str(input("name: "))
bas_sal = int(input("BS : "))

HRA = (0.4*bas_sal)
DA = (0.1*bas_sal)
CCA = (0.5 * bas_sal)

GS = bas_sal+HRA +DA +CCA

PF = (0.1*GS)
IT = (0.1*GS)
NS = (GS-(PF+IT))


print(HRA ,DA,CCA,GS,PF,IT,NS)
