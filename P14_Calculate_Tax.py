#14. Write a Python program to accept a person's annual income and calculate the tax payable according to different income slabs. 


income = int(input("Enter Annual Income: "))

if income <= 300000:
    tax = 0


elif income <= 700000:
    tax = (income - 300000) * 0.05


elif income <= 1000000:
   
    tax = 20000 + (income - 700000) * 0.10


else:
    # 50,000 is the accumulated tax from all previous slabs (20,000 + 30,000)
    tax = 50000 + (income - 1000000) * 0.15


print("Payable Tax:", tax)
