n = int(input("Enter the number:"))

for i in range(1, n + 1):
    # Print spaces before the stars
    print(" " * (n - i), end="")
    # Print stars
    print("*" * i)



# OUTPUT :-
# Enter the number:5
#    *
#   **
#   ***
#  ****
# *****