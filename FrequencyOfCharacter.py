text = input("Enter a string: ")  
freq = {}

for char in text:  
    freq[char] = freq.get(char, 0) + 1  # Use .get() to handle missing characters

print("Character frequencies:", freq)


# OUTPUT :-
# Enter a string: ankana
# Character frequencies: {'a': 3, 'n': 2, 'k': 1}