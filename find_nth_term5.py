import math

def find_nth_term(n):
    return math.factorial(n)

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")


#OUTPUT :-
#Enter the value of n: 6
#The 6th term of the sequence is: 720