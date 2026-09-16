#15. Write a Python program to accept monthly mobile data data_usage in GB and calculate the total bill according to specified data_usage slabs.

data_usage = float(input("Enter monthly mobile data usage (in GB): "))

if data_usage <=5:
    bill = data_usage *10
elif data_usage <=10:
    bill = (5*10) + (data_usage - 5)*8
elif data_usage <=20:
    bill = (5*10) + (5*8) + (data_usage - 10)*6
else:
    bill = (5*10)+(5*8)+(10*6)+(data_usage - 20)*6

print("Monthly Data Usage:", data_usage, "GB")
print("Total Payable bill: Rs",bill)
