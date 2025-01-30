import math

def sum_of_factorials(n):
    total = 0
    for i in range(1, n+1):
        total += math.factorial(i)
    return total

# Example usage:
n = int(input("Enter a number: "))
result = sum_of_factorials(n)
print(f"The sum of factorials from 1! to {n}! is: {result}")


#Output :- 
#Enter a number: 5
#The sum of factorials from 1! to 5! is: 153