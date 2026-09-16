#17. Write a Python program to accept an integer and determine whether it is a palindrome using a `while` loop.

num = int(input("Enter Number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if rev == temp:
    print(temp," is Palindrome")
else:
    print(temp," is not Palindrome")