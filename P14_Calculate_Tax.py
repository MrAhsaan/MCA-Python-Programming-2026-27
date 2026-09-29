#14. Write a Python program to accept a person's annual income and calculate the tax payable according to different income slabs. 

# Accept Annual Income from the user
income = int(input("Enter Annual Income: "))

# Slab 1: 0 to 3,00,000 -> 0% Tax
if income <= 300000:
    tax = 0

# Slab 2: 3,00,001 to 7,00,000 -> 5% Tax
elif income <= 700000:
    tax = (income - 300000) * 0.05

# Slab 3: 7,00,001 to 10,00,000 -> 10% Tax
elif income <= 1000000:
    # 20,000 is the maximum tax from the previous slab (4,00,000 * 0.05)
    tax = 20000 + (income - 700000) * 0.10

# Slab 4: Above 10,00,000 -> 15% Tax
else:
    # 50,000 is the accumulated tax from all previous slabs (20,000 + 30,000)
    tax = 50000 + (income - 1000000) * 0.15

# Display final result
print("Payable Tax:", tax)
