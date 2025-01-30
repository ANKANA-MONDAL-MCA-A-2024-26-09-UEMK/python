n = int(input("Enter the number:"))

for x in range(n):
    rx = 1
    print(" " * (n - x - 1), end="")  # Print spaces for alignment
    for y in range(x + 1):
        print(rx, end=" ")
        rx = rx * (x - y) // (y + 1)  # Formula to calculate binomial coefficients
    print()  # Move to the next line after each row



#OUTPUT :-
# Enter the number:5
#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1