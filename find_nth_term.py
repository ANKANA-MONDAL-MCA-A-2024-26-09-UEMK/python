def find_nth_term(n):
    if n % 2 == 1:  # Odd index term
        if n == 1:
            return 2
        elif n == 3:
            return 3
        else:
            # Pattern for odd indexed terms is 2, 3, 15, ...
            prev_odd = 2
            for i in range(3, n + 1, 2):
                prev_odd = prev_odd * (i)
            return prev_odd
    else:  # Even index term
        return 4

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")


#OUTPUT :-
#Enter the value of n: 6
#The 6th term of the sequence is: 4