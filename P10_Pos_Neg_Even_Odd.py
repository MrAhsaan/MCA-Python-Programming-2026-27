#10. Write a Python program to accept an integer and determine whether it is positive, negative, even, odd, or zero.

num = int(input("Enter an Integer: "))

if num>0:
    print("POSITIVE +")
elif num<0:
    print("NEGATIVE -")
else:
    print("ZERO 0")

if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")
