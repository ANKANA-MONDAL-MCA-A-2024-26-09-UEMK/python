def binary_search(arr, x):
    low, high = 0, len(arr) - 1  

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == x:
            return mid  
        elif arr[mid] < x:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1  

arr = [10, 20, 30, 40, 50]  
num = int(input("Enter number to search: "))  
result = binary_search(arr, num)  

if result != -1:
    print("Found at index", result)  
else:
    print("Not found")  
