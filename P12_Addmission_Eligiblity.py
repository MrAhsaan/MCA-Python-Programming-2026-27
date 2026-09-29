#12. Write a Python program to accept marks obtained in Mathematics, Physics, and Chemistry and determine whether a student is eligible for admission based on subject-wise and overall percentage requirements.

math = float(input("Enter Marks of Mathemetics: "))
chem = float(input("Enter Marks of Chemistry: "))
phy = float(input("Enter Marks of Physics: "))

min_math_marks = 60
min_chem_marks = 50
min_phy_marks = 50
min_percentage = 60
max_Total_marks = 300

total_obtained_marks = math + chem + phy
percentage = (total_obtained_marks / max_Total_marks)*100

print("Total Marks: ",total_obtained_marks)
print(f"Percentage: {percentage:.2f}%")

if(math>=min_math_marks) and (chem>=min_chem_marks) and (phy>=min_phy_marks) and percentage>=min_percentage :
    print("You are Eligible for Admission")
else:
    print("You are not Eligible for Admission")
