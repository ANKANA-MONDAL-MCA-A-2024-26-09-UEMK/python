def find_nth_term(n):
    if n % 2 == 1:  # Odd index term
        return 0
    else:  # Even index term
        # For even indices: observed pattern follows the series 6, 12, 90, ...
        if n == 2:
            return 6
        elif n == 4:
            return 12
        elif n == 6:
            return 90
        else:
            # For higher even indices, you may need to define a further pattern if it continues.
            # Example placeholder for now: Can return a factor or generate based on your observation.
            return "Pattern continues..."

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")

#OUTPUT :-
#Enter the value of n: 2
#The 2th term of the sequence is: 6