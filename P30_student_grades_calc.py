#30. Write a Python program to accept the marks of N students and calculate the class average, highest marks, lowest marks, number of passed and failed students, and number of students scoring above 75%.

n = int(input("Enter the total number of students: "))

# Initialize variables
total_marks = 0
passed_students = 0
failed_students = 0
distinction_students = 0  # Above 75%

# Set initial tracking limits (assuming marks are out of 100)
highest_marks = -1
lowest_marks = 101

# Loop to collect data for each student
for i in range(1, n + 1):
    marks = float(input(f"Enter marks for student {i}: "))
    
    total_marks += marks
    
    # Track highest and lowest
    if marks > highest_marks:
        highest_marks = marks
    if marks < lowest_marks:
        lowest_marks = marks
        
    # Check passing criteria (assuming 40 is passing)
    if marks >= 40:
        passed_students += 1
    else:
        failed_students += 1
        
    # Check distinction (> 75)
    if marks > 75:
        distinction_students += 1

# Final Calculations
class_average = total_marks / n

print("\n--- CLASS PERFORMANCE REPORT ---")
print(f"Class Average Marks: {class_average:.2f}")
print(f"Highest Marks Obtained: {highest_marks}")
print(f"Lowest Marks Obtained: {lowest_marks}")
print(f"Total Passed Students: {passed_students}")
print(f"Total Failed Students: {failed_students}")
print(f"Students Scoring Above 75%: {distinction_students}")
