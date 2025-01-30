import math

def sum_of_series(x, n):
    total = 0
    for i in range(n + 1):
        exponent = 2 * i  # The exponent increases by 2 each time
        sign = (-1) ** i  # Alternate the signs
        total += sign * (x ** exponent) / math.factorial(exponent)
    return total

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))
result = sum_of_series(x, n)
print(f"The sum of the series 1 - x^2/2! + x^4/4! - x^6/6! + ... up to {n} terms is: {result}")


#OUTPUT :-
#Enter the value of x: 6
#Enter the number of terms (n): 4
#The sum of the series 1 - x^2/2! + x^4/4! - x^6/6! + ... up to 4 terms is: 13.857142857142861