#7. Write a Python program to accept three numbers and determine the largest and smallest number using decision-making statements.


n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))

if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

if n1 <= n2 and n1 <= n3:
    smallest = n1
elif n2 <= n1 and n2 <= n3:
    smallest = n2
else:
    smallest = n3

print("\nLargest Number: ",largest)

print("Smallest Number : ",smallest)
