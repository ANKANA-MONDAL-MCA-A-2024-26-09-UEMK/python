import math

def sum_of_series(n):
    total = 0
    for i in range(1, n+1):
        total += i / math.factorial(i)
    return total

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_series(n)
print(f"The sum of the series 1/1! + 2/2! + 3/3! + ... + {n}/{n}! is: {result}")


#OUTPUT :- 
#Enter a number: 6
#The sum of the series 1/1! + 2/2! + 3/3! + ... + 6/6! is: 2.7166666666666663