# Question B17: WAP to input the marks of a student in five subjects and calculate the grade according the following conditions:
# 		Marks						Grade
# 		>90						S
# 		76-90						A
# 		61-75						B
# 		51-60						C
# 		40-50						D
# 		<40						Fail
marks1= int(input("mark in sub1: "))
marks2=int(input("mark  in sub2: "))
marks3= int(input("mark in sub3: "))
marks4= int(input("mark in sub4: "))
marks5= int(input("mark in sub5: "))
total = ((marks1+marks2+marks3+marks4+marks5)/500)*100

if(total>90):
    print("Grade S")
elif(total>76 and total<90):
    print("Grade A")
elif(total>61 and total<75):
    print("Grade B")
elif (total>51 and total<60):
    print("Grade C")
elif (total>40 and total<51):
    print("Grade D")
else:
    print("Fail")



