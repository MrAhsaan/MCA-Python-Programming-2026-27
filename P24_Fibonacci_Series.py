#24. Write a Python program to accept the number of terms and generate the Fibonacci series using a `for` loop. Also calculate the sum of the generated terms.

num = int(input("Enter Number of Terms: "))
a = 0
b = 1
sum = 0
print("Fibonacci Series:")
for i in range(num):
    print(a, end = ' ')
    sum = sum + a
    c = a+b
    a = b
    b = c
print("\nSum of generated terms",sum)
