def find_nth_term(n):
    if n % 2 == 1:  # Odd index term
        return 2 * ((n + 1) // 2 - 1)
    else:  # Even index term
        return (n // 2) - 1

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")


#OUTPUT :-
#Enter the value of n: 6
#The 6th term of the sequence is: 2