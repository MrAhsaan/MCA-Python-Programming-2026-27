#3. Write a Python program to accept the number of electricity units consumed by a consumer and calculate the electricity bill according to different consumption slabs.

units = float(input("Enter Electricity Unit: "))

fixed_charge = 100
tax = 0.10
energy_charges = 0

if units <= 100:
    # Slab 1: Up to 100 units
    energy_charges = units * 3.00
elif units <= 300:
    # Slab 2: First 100 units at 3.00, remaining at 5.00
    energy_charges = (100 * 3.00) + ((units - 100) * 5.00)
else:
    # Slab 3: First 100 at 3.00, next 200 at 5.00, remaining at 8.00
    energy_charges = (100 * 3.00) + (200 * 5.00) + ((units - 300) * 8.00)

Electric_Tax = energy_charges * tax
Electric_Bill = energy_charges + Electric_Tax + fixed_charge

print("Unit: ",units)
print("Fixed Charge: ",fixed_charge)
print("Tax: ",Electric_Tax)
print("Total Electricty Bill: ",Electric_Bill)