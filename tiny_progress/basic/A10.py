# Question A10: WAP to input the number the days from the user and convert it into years, weeks, and days.

def conversion(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

days = int(input("Days: "))

years, weeks, remaining_days = conversion(days)

print(f'{days} are equal to : {years}: years, {weeks}: weeks and {remaining_days}: remaining days ')