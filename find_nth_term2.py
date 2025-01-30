def find_nth_term(n):
    if n % 2 == 1:  # Odd index term
        if n == 1:
            return 3
        else:
            # Odd-index terms seem to increase with a decreasing difference
            prev_odd = 3
            increment = 30  # Initial increment
            for i in range(3, n + 1, 2):
                prev_odd += increment
                increment -= 10  # Decrease the increment by 10 each time
            return prev_odd
    else:  # Even index term
        prev_even = 5
        increment = 30
        for i in range(4, n + 1, 2):
            prev_even += increment
        return prev_even

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")



#OUTPUT :-
#Enter the value of n: 5
#The 5th term of the sequence is: 53