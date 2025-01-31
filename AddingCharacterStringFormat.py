text = input("Enter a string: ")
shift = int(input("Enter shift number: "))
encoded_text = ""

for char in text:
    new_char = char
    if 'a' <= char <= 'z':  # Lowercase letters
        new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    elif 'A' <= char <= 'Z':  # Uppercase letters
        new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    
    encoded_text += new_char  # Add the encoded character to the result

print("Encoded string:", encoded_text)
