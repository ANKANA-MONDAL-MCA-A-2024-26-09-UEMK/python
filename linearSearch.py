arr = [10, 20, 30, 40, 50]  
num = int(input("Enter number to search: "))  
found = False  

for i in range(len(arr)):  
    if arr[i] == num:  
        print("Found at index", i)  
        found = True  
        break  # Stops searching once the number is found

if not found:  
    print("Not found")  
