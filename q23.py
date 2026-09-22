#23. Write a Python program to accept two integers representing a range and display all prime numbers within that range. Also display the total number of prime numbers found.

start = int(input("Enter First range: "))
end = int(input("Enter Last range: "))

count = 0

print(f"\nPrime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                break  
        else:
            print(num, end=" ")
            count += 1

print(f"\n\nTotal number of prime numbers found: {count}")
