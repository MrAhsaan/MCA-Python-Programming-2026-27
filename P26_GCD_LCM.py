#26. Write a Python program to accept two positive integers and calculate their GCD and LCM using iterative statements.

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))


a = num1
b = num2

# Iterative GCD calculation (Euclidean Algorithm)
while b > 0:
    remainder = a % b
    a = b
    b = remainder

gcd = a
lcm = (num1 * num2) // gcd

print(f"\nGCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
