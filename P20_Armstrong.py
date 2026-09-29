#20. Write a Python program to accept an integer and determine whether it is an Armstrong number.

num = int(input("Enter an Integer: "))
temp = num
count = len(str(temp))
sum = 0
while num > 0:
    rem = num % 10
    prod = rem ** count
    sum = sum + prod
    num = num // 10
if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
