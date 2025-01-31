num = input("Enter a 10-digit number: ")  

# Ensure the input is exactly 10 digits
if num.isdigit() and len(num) == 10:
    max_digit = max(num)  
    print("Maximum digit:", max_digit)  
else:
    print("Invalid input! Please enter a 10-digit number.")


# OUTPUT :-
# Enter a 10-digit number: 9128736543
# Maximum digit: 9