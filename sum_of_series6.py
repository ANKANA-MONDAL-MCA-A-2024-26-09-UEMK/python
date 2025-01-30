def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 1:  # If i is odd, add the term
            total += 1 / i
        else:  # If i is even, subtract the term
            total -= 1 / i
    return total

# Example usage:
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(n)
print(f"The sum of the series 1 - 1/2 + 1/3 - 1/4 + ... up to {n} terms is: {result}")


#OUTPUT :-
#Enter the number of terms (n): 5
#The sum of the series 1 - 1/2 + 1/3 - 1/4 + ... up to 5 terms is: 0.7833333333333332     