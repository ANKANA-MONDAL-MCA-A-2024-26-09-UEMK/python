# Program to Sort a List of Dictionaries by a Key

def sort_dict_by_key(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

# Example Usage
list_of_dicts = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 18}, {"name": "Charlie", "age": 30}]
sorted_list = sort_dict_by_key(list_of_dicts, "age")
print(sorted_list)
