#18. Write a Python program to accept an integer and calculate the sum and product of all its digits using a `while` loop.

num = int(input("Enter an Integer: "))
sum = 0
product = 1

while num > 0:
    rem = num % 10
    sum = sum + rem
    product = product * rem
    num = num // 10
print("Sum of Integer is: ",sum)
print("Product of Integer is: ",product)
