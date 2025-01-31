arr = list(map(int, input("Enter numbers separated by spaces: ").split()))  
n = len(arr)

for i in range(n):  
    min_index = i  
    for j in range(i + 1, n):  
        if arr[j] < arr[min_index]:  
            min_index = j  
    arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element with the first element  

print("Sorted array:", arr)  
