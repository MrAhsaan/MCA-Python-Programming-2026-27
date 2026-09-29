#11. Write a Python program to accept a person's age, monthly income, and credit score and determine whether the person is eligible for a loan based on specified conditions.

age = int(input("Enter Person's Age: "))
monthly_income = int(input("Enter Monthly Income: "))
credit_score = int(input("Enter Credit Score: "))

if (age > 21 and age <60) and (monthly_income > 15000) and (credit_score >= 700):
    print("congrats!! You are Eliglible to take Loan...")
else:
    print("Sorry!! You are not Eligible for Loan..")
