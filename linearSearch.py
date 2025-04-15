def linearSearch(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:  # Corrected indexing
            return i
    return -1    

arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
n = len(arr)
x = int(input("Enter a number to search in the array: "))  # Convert input to integer

result = linearSearch(arr, n, x)

if result != -1:
    print(f"The element is found at index {result}")
else:
    print("Element not found")


