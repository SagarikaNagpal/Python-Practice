# to input the number the days from the user and convert it into years, weeks and days.

days = int(input("days:  "))

year = days/365
days = days%365

week = days/7
days = days%7
day = days

print("year",year)
print("week",week)
print("day",day)

