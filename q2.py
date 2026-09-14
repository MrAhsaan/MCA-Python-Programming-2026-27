#2. Write a Python program to accept an employee's basic salary and calculate DA, HRA, gross salary, tax deduction, and net salary

basic_salary = int(input("Enter Basic Salary: "))

DA = basic_salary * 0.40
HRA = basic_salary * 0.20
Gross_salary = basic_salary + DA + HRA
tax_deduction = basic_salary * 0.10

Net_Salary = Gross_salary - tax_deduction

print("DA: = ",DA)
print("HRA: = ",HRA)
print("Gross_salary: =",Gross_salary)
print("Net_salary: =",Net_Salary)