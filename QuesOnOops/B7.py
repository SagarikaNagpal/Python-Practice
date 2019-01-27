# Question B7: WAP to input the name and age of a person and display “CHILD” or “TEENAGER” according to the age.

name = str(input("name: "))
age = int(input("age: "))

if(age>=13):
    print("Teenager")

else:
    print("child")