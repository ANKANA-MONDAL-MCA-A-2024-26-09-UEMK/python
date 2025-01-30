def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def clone_list(lst):
    return lst[:]

def count_occurrences(lst):
    return {x: lst.count(x) for x in set(lst)}

def remove_multiple_elements(lst, elements):
    return [x for x in lst if x not in elements]

def remove_duplicates(lst):
    return list(set(lst))

def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def are_lists_identical(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

def max_min_positions(lst):
    max_pos = lst.index(max(lst))
    min_pos = lst.index(min(lst))
    return max_pos, min_pos

# User input:
lst = list(map(int, input("Enter a list of numbers (space separated): ").split()))
print("Interchanged list:", interchange_first_last(lst))
print("Cloned list:", clone_list(lst))
print("Occurrences count:", count_occurrences(lst))
remove_elements = list(map(int, input("Enter elements to remove (space separated): ").split()))
print("List after removal:", remove_multiple_elements(lst, remove_elements))
print("List without duplicates:", remove_duplicates(lst))
print("Second largest number:", second_largest(lst))
lst2 = list(map(int, input("Enter another list for comparison (space separated): ").split()))
print("Intersection of lists:", intersection(lst, lst2))
print("Are lists identical?:", are_lists_identical(lst, lst2))
print("Max and Min positions:", max_min_positions(lst))
