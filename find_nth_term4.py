def find_nth_term(n):
    if n % 2 == 1:  # Odd index term
        return 14 + (n // 2) * 6
    else:  # Even index term
        return 28 + ((n // 2) - 1) * 12

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")



#OUTPUT :-
#Enter the value of n: 4
#The 4th term of the sequence is: 40