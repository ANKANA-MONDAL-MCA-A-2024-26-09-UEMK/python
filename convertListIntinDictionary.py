# Program to Convert a List into a Dictionary

def list_to_dict(lst):
    return {i: lst[i] for i in range(len(lst))}

# Example Usage
lst = ['apple', 'banana', 'cherry']
result = list_to_dict(lst)
print(result)
