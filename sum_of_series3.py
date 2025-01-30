def sum_of_series3(x, n):
    total = 0
    for i in range(n + 1):
        total += x ** i
    return total

# Example usage:
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
result = sum_of_series3(x, n)
print(f"The sum of the series 1 + x + x^2 + x^3 + ... + x^{n} is: {result}")


#OUTPUT :-
#Enter the value of x: 5
#Enter the value of n: 4
#The sum of the series 1 + x + x^2 + x^3 + ... + x^4 is: 781.0