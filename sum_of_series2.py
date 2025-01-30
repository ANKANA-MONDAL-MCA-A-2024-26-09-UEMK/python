def sum_of_series2(n):
    total = 0
    for i in range(1, n+1):
        total += i / (i ** i)
    return total

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_series2(n)
print(f"The sum of the series 1/1^1 + 2/2^2 + 3/3^3 + ... + {n}/{n}^{n} is: {result}")


#OUTPUT :- 
#Enter a number: 6
#The sum of the series 1/1^1 + 2/2^2 + 3/3^3 + ... + 6/6^6 is: 1.6284647119341564