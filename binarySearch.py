#function 
def binarySearch(arr, target):
    i =0 
    j= len(arr)-1

    while i <= j:
        mid = (i+j)//2
        if arr[mid] == target:
            return mid 
        elif arr[mid]< target :
            left = mid +1
            
        else :
            right = mid-1 
         
    return -1            

# DRIVER CODE 
arr= [20,22,33,45,66,78,92,103]
target = 78
result =binarySearch(arr, target)

if result != 1:
     print ("target element {target}found at {result}")
else:
    print("not found !!!")   
