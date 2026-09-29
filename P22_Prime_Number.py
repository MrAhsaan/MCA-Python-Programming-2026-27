#22. Write a Python program to accept an integer and determine whether it is a prime number using a `for` loop.

num = int(input("Enter an Integer: "))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not Prime")
