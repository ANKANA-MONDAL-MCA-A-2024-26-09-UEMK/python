n = int(input("Enter the number:"))
k = 2 * n - 2

# Upper part of the diamond
for i in range(0, n):
    # Print spaces before the stars
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    
    # Print the stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")  # Move to the next line

# Lower part of the diamond
k = n - 2
for i in range(n, -1, -1):
    # Print spaces before the stars
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    
    # Print the stars
    for j in range(0, i + 1):
        print("* ", end="")
    print("")  # Move to the next line



#OUTPUT :- 
#Enter the number:8
#              *
#             * *
#           * * *
#           * * * *
#          * * * * *
#         * * * * * *
#        * * * * * * *
#       * * * * * * * *
#      * * * * * * * * *
#       * * * * * * * *
#        * * * * * * *
#         * * * * * *
#          * * * * *
#           * * * *
#            * * *
#             * *
#              *   