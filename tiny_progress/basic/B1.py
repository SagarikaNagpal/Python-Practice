'''def calculate_result(marks):
    total_marks = 500  # Assuming total marks for all subjects is 500
    passing_marks_percentage = 40
    passing_marks = (passing_marks_percentage / 100) * total_marks

    if marks >= passing_marks:
        return "Pass"
    else:
        return "Fail"

# Input marks from the user
marks = float(input("Enter the marks obtained: "))

# Calculate and print the result
result = calculate_result(marks)
print("Result:", result)'''
# Question B1: WAP to input the marks of a student and print the result (passing marks = 40 %).

def passingCriteria(m,e,sc):

    total_marks = maths+english+sc
    print('Total_marks: ',total_marks)
    passing_marks_percentage = 40
    passing_marks = (passing_marks_percentage / 100) * total_marks
    print('Passing_marks: ',passing_marks)

    if total_marks> passing_marks:
        print("Pass")
    else:
        print('fail')
maths = float(input('Maths: '))
english = float(input('English: '))
sc = float(input('Science: '))
passingCriteria(maths,english,sc)
