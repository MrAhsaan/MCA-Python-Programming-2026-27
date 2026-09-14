#6. Write a Python program to accept a student's percentage and display the appropriate grade using `if-elif-else` statements. Also validate that the percentage is between 0 and 100.

student_percentage = float(input("Enter Percentage 0 to 100: "))

if student_percentage < 0 or student_percentage > 100:
    print("Invalid Input! Percentage must be between 0 and 100.")

elif student_percentage >= 90:
    print("GRADE A")
elif student_percentage >= 80:
    print("GRADE B")
elif student_percentage >= 70:
    print("GRADE C")
elif student_percentage >= 60:
    print("GRADE D")
elif student_percentage >= 50:
    print("GRADE E")
else:
    print("Failed")
