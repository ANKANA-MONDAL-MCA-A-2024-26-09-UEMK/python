n = int(input("Enter the number:"))

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print stars with spaces in between
    for j in range(i):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()


#OUTPUT :-
#Enter the number:6
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *