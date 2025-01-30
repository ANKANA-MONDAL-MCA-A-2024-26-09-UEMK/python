n = int(input("Enter the number:"))
r = n // 2 + 1

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if y == r or y == n - r + 1:
            print("*", end="")
        else:
            print(" ", end="")
    
    # Adjust the value of r based on the row number
    if x <= n // 2:
        r -= 1
    else:
        r += 1
    
    print()  # Move to the next line after each row
