#5. Write a Python program to accept the price and quantity of three products and calculate the subtotal, discount, GST, and final payable amount.

item_total_list = []

for i in range(1, 4):
    
    price = float(input(f"Enter Price of Product{i}: ")) 
    quantity = int(input(f"Enter Quantity of Product{i}: "))
    item_total = price * quantity
    item_total_list.append(item_total)
sub_total = sum(item_total_list)

discount_rate = 0.10
GST = 0.18
discount_amt = sub_total * discount_rate
discounted_price = sub_total - discount_amt

gst_amt = discounted_price * GST 
total_payable = discounted_price + gst_amt

print("\n--- BILL ---")
print("Sub Total    : ", round(sub_total, 2))
print("Discount (-) : ", round(discount_amt, 2))
print("GST (+)      : ", round(gst_amt, 2))
print("Total Payable: ", round(total_payable, 2))
