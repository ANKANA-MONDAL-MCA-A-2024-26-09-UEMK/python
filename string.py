def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

def reverse_words(s):
    return " ".join(s.split()[::-1])

def print_even_length_words(s):
    return [word for word in s.split() if len(word) % 2 == 0]

def remove_ith_character(s, i):
    return s[:i] + s[i+1:] if 0 <= i < len(s) else s

def is_symmetrical_or_palindrome(s):
    return s == s[::-1]

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def replace_except(lst, char, replacement):
    return [char if x == char else replacement for x in lst]

# User input:
s = input("Enter a string: ")
print("Without duplicates:", remove_duplicates(s))
print("Reversed words:", reverse_words(s))
print("Even length words:", print_even_length_words(s))
i = int(input("Enter index to remove character: "))
print("String after removing character:", remove_ith_character(s, i))
print("Is palindrome or symmetrical:", is_symmetrical_or_palindrome(s))
s1 = input("Enter first string for anagram check: ")
s2 = input("Enter second string for anagram check: ")
print("Are they anagrams?:", are_anagrams(s1, s2))
user_char = input("Enter character to keep: ")
replacement_char = input("Enter replacement character: ")
lst = list(input("Enter a list of characters (comma separated): ").split(","))
print("Replace all except given character:", replace_except(lst, user_char, replacement_char))
