# Question A17: WAP to input inches from the user and convert it into yards, feet and cm.
'''1 inch = 0.0277778 yards
1 inch = 0.0833333 feet
1 inch = 2.54 centimeters'''

def conversion(inch):

    yards = round(inch * 0.0277778,3)
    feet = round(inch * 0.0833333,3)
    cm = round(inch * 2.54,3)
    print(f'{inch} = yards: {yards}, feet: {feet} and cm: {cm}')
inch = float(input("inches: "))

conversion(inch)
