num = input("Enter a 4-digit number: ")  
even_digits = []  
odd_digits = []  

for digit in num:  
    if int(digit) % 2 == 0:  
        even_digits.append(digit)  
    else:  
        odd_digits.append(digit)  

print("Even digits:", even_digits)  
print("Odd digits:", odd_digits)  
print("Total even digits:", len(even_digits))  
print("Total odd digits:", len(odd_digits))  


#OUTPUT :-
# Enter a 4-digit number: 2005
# Even digits: ['2', '0', '0']
# Odd digits: ['5']
# Total even digits: 3
# Total odd digits: 1