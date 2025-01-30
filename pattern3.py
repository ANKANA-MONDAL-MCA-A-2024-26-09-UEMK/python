n = int(input("Enter number of n:"))
number = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(number, end="")
        number += 1
    print()



# OUTPUT :-
# Enter number of n:5
# 1
# 23
# 456
# 78910
# 1112131415