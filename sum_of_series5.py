def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i * (i + 1) * (i + 2)
    return total

# Example usage:
n = int(input("Enter the value of n: "))
result = sum_of_series(n)
print(f"The sum of the series 1*2*3 + 2*3*4 + ... + n*(n+1)*(n+2) is: {result}")


#OUTPUT :-
#Enter the value of n: 5
#The sum of the series 1*2*3 + 2*3*4 + ... + n*(n+1)*(n+2) is: 420