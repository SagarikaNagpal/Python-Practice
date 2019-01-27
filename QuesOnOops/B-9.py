# Question B9: WAP to input marks in five subjects of a student and calculate the division according to the following conditions:
# 		Percentage				Division
# 		>=60					First
# 		50-59					Second
# 		40-49					Third
# 		<40					Fail
eng = int(input("eng: "))
hindi = int(input("hindi: "))
maths = int(input("maths: "))
sst = int(input("sst: "))
science = int(input("science: "))
total = (((eng+hindi+maths+sst+science)/500))*100
print(total)
if(total >= 60):
    print("first div")
elif(total>50 and total<59):
    print("2nd div")
elif(total>40 and total<49):
    print("3rd div")
else:
    print("fail")
