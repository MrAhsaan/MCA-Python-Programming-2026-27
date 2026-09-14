# 1. Write a Python program to accept the marks obtained by a student in five subjects and calculate the total marks, average marks, and percentage.

s1 = int(input("Enter Marks of subject1 "))
s2 = int(input("Enter Marks of subject2 "))
s3 = int(input("Enter Marks of subject3 "))
s4 = int(input("Enter Marks of subject4 "))
s5 = int(input("Enter Marks of subject5 "))

total_marks = s1+s2+s3+s4+s5
avg = (total_marks/5)
percentage = (total_marks/500)*100
print("Total Obtained Marks: ",total_marks)
print("Average: ",avg)
print("Percentage: ",percentage)
