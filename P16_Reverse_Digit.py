#16. Write a Python program to accept an integer and reverse its digits using a `while` loop.

num = int(input("Enter an Integer: "))
rev = 0
while num > 0:
    rem = num % 10  #565 56 5 0....0,5,6,5
    rev = rev * 10 + rem
    num = num // 10

print("Reversed Number: ",rev)
