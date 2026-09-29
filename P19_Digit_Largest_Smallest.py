#19. Write a Python program to accept an integer and find the number of digits, largest digit, and smallest digit using a `while` loop.

org_num =int(input("Enter an Ineger: "))
num = abs(org_num)

count = 0
largest = 0
smallest = 9

if num == 0:
    count = 1
    smallest = 0
else:
    while num > 0:
        rem = num % 10

        if rem > largest:
            largest = rem
        if rem < smallest:
            smallest = rem
        count += 1
        num = num // 10
print("Number of digit: ",count)
print("Largest digitL: ",largest)
print("Smallest Digit: ",smallest)
