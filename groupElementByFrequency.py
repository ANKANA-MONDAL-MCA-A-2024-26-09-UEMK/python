# Program to Group Elements by Frequency

from collections import defaultdict,Counter

def group_by_frequency(lst):
    freq_dict = defaultdict(list)
    counter = Counter(lst)
    for key, value in counter.items():
        freq_dict[value].append(key)
    return dict(freq_dict)

# Example Usage
lst = [1, 2, 2, 3, 3, 3, 4]
result = group_by_frequency(lst)
print(result)
