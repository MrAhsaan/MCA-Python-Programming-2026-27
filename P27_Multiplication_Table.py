#27. Write a Python program using nested `for` loops to display multiplication tables from 1 to 10 in a structured tabular format.

print("Multiplication Tables from 1 to 10:\n")

# Outer loop for rows (multipliers 1 to 10)
for row in range(1, 11):
    # Inner loop for columns (tables 1 to 10)
    for col in range(1, 11):
        product = row * col
        # print with a tab space to keep columns aligned
        print(f"{col}x{row}={product}", end="\t")
    print()  # Move to the next row
