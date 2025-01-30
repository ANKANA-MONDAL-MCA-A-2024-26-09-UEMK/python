import string

def find_nth_term(n):
    # Create the alphabet list
    alphabet = string.ascii_lowercase

    # Initialize the count for the current letter's repetition
    count = 1
    i = 0

    # Determine which letter corresponds to the nth term
    while n > count:
        n -= count  # Decrease n by the number of times the current letter repeats
        count += 1  # Next letter will repeat count+1 times
        i += 1  # Move to the next letter in the alphabet

    # Return the corresponding letter
    return alphabet[i]

# Example usage:
n = int(input("Enter the value of n: "))
result = find_nth_term(n)
print(f"The {n}th term of the sequence is: {result}")


#OUTPUT :-
#Enter the value of n: 2
#The 2th term of the sequence is: b