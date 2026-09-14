# 1. Write a Python program to accept the marks obtained by a student in five subjects and calculate the total marks, average marks, and percentage.

marks = []
for i in range(1,6):
    subject_marks = float(input(f"Enter marks of Subject{i} "))
    marks.append(subject_marks)
print(marks)

total_marks = sum(marks)
print("Total Marks = ",total_marks)

avg = total_marks / len(marks)
print("Average Marks = ",avg)

#max_marks = len(marks)*100
#percentage = (total_marks / max_marks)*100
percentage = (total_marks/(len(marks)*100)*100)
print(f"Percentage      : {percentage:.2f}%")
