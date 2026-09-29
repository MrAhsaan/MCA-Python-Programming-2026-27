 #28. Write a Python program using nested loops to generate a number pattern for `n` rows, where `n` is entered by the user.

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1,i + 1):
        print(j, end=" ")
    print()  
