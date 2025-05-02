# Program to Find the Most Frequent Element in a List

from collections import Counter

def most_frequent_element(lst):
    counter = Counter(lst)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None

# Example Usage
lst = [1, 2, 2, 2, 3, 3, 3, 4]
result = most_frequent_element(lst)
print(result)
