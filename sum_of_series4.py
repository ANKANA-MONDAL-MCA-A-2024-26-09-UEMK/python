def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (2 * i - 1) * (2 * i + 1)
    return total

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series 1*3 + 3*5 + 5*7 + ... up to {n} terms is: {result}")


#OUTPUT :-
#Enter the number of terms (n): 5
#The sum of the series 1*3 + 3*5 + 5*7 + ... up to 5 terms is: 215