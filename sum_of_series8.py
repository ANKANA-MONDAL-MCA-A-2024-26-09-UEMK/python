def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += 3 * i**2 - 3 * i + 1
    return total

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series 1 + 2 + 11 + 26 + 47 + ... up to {n} terms is: {result}")


#OUTPUT :-
#Enter the number of terms (n): 4
#The sum of the series 1 + 2 + 11 + 26 + 47 + ... up to 4 terms is: 64