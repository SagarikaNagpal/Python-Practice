# Question B9: WAP to input marks in five subjects of a student and calculate the division according to the following conditions:
# 		Percentage				Division
# 		>=60					First
# 		50-59					Second
# 		40-49					Third
# 		<40					Fail

math = int(input("maths:"))
hindi = int(input("hindi"))
eng = int(input("eng"))
sst = int(input("sst"))
scie = int(input("sci"))
total= ((math+hindi+sst+scie+eng)/500*100)
print(total)

if(total>=60):
    print("First")
elif(total>=50 and total<=59):
    print("second")
elif (total>= 40 and total <=49):
    print("third")
else:
    print("Fail")

