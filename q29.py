#29. Write a Python program to create a menu-driven mathematical application with options to check Prime, Palindrome, Armstrong, Factorial, Fibonacci Series, and Exit. The menu should be displayed repeatedly until the user selects Exit.

choice = 0

while choice != 6:
    print("\n--- MATHEMATICAL MENU ---")
    print("1. Check Prime Number")
    print("2. Check Palindrome Number")
    print("3. Check Armstrong Number")
    print("4. Find Factorial")
    print("5. Generate Fibonacci Series")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        num = int(input("Enter a number: "))
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    print(f"{num} is not a Prime number.")
                    break
            else:
                print(f"{num} is a Prime number.")
        else:
            print(f"{num} is not a Prime number.")
            
    elif choice == 2:
        num = int(input("Enter a number: "))
        temp = num
        reverse = 0
        while temp > 0:
            digit = temp % 10
            reverse = (reverse * 10) + digit
            temp //= 10
        if num == reverse:
            print(f"{num} is a Palindrome.")
        else:
            print(f"{num} is not a Palindrome.")
            
    elif choice == 3:
        num = int(input("Enter a number: "))
        temp = num
        num_str = str(num)
        power = len(num_str)
        arm_sum = 0
        while temp > 0:
            digit = temp % 10
            arm_sum += digit ** power
            temp //= 10
        if num == arm_sum:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
            
    elif choice == 4:
        num = int(input("Enter a number: "))
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"Factorial of {num} is {factorial}")
        
    elif choice == 5:
        terms = int(input("Enter number of terms: "))
        x, y = 0, 1
        print("Fibonacci Series:", end=" ")
        for i in range(terms):
            print(x, end=" ")
            next_term = x + y
            x = y
            y = next_term
        print()
        
    elif choice == 6:
        print("Exiting application. Goodbye!")
    else:
        print("Invalid choice! Please select between 1 and 6.")
