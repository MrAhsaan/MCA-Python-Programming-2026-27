#25. Write a Python program to accept an integer and display all its factors. Also display the total number of factors.

n = int(input("Enter an Integer: "))
fact = 0

print(f"Factors of {n} is: ")
for i in range(1,n+1):
    if n % i ==0:
        print(i, end = ' ')
        fact += 1
print("\nTotal number of Factors is ",fact)
