n = int(input("Enter the number:"))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")  # Print stars on the border
        else:
            print(" ", end="")  # Print spaces inside
    print()  # Move to the next line after each row


#OUTPUT :-
# Enter the number:5
# *****
# *   *
# *   *
# *   *
# *****