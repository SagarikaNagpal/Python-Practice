# WAP to input principle, rate and time from the user and calculate the simple interest and total amount. Display all the values.

p= int(input("p: "))
r= int(input("r: "))
t= int(input("t: "))

SI = (p*r*t)/100
TA = (p+t)

print("SI: ",SI)
print("TA",TA)