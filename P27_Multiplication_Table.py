#27. Write a Python program using nested `for` loops to display multiplication tables from 1 to 10 in a structured tabular format.

print("Multiplication Tables from 1 to 10:\n")


for row in range(1, 11):
    
    for col in range(1, 11):
        product = row * col
        
        print(f"{col}x{row}={product}", end="\t")
    print() 
