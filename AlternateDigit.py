num = input("Enter a 10-digit number: ")  

# Ensure the input is exactly 10 digits
if num.isdigit() and len(num) == 10:
    print("Alternate digits:", num[::2])  
else:
    print("Invalid input! Please enter a 10-digit number.")
