''' Recursive algorithm that splits array into half until it cannot, sorts them and merges them into a single array'''

# Optimal for large data sets
# Time complexity : O(n log n) -> 2 T(n/2) + θ(n)
# Space Complexity : O(n)

def mergesort(arr):
    if len(arr) > 1:
        
        # Finding the mid of array to divide into 2 halves
        mid = len(arr) // 2
        
        # Divide arrays into 2 halves
        leftArr, rightArr = arr[:mid], arr[mid:]
        
        # Recursively sort the left and right halves
        mergesort(leftArr) # T(n/2)
        mergesort(rightArr) # T(n/2)

        ### -- Dividing part complete -- ##

        i = j = k = 0

        # Loop throgh left and right arrays and merge according to their sort order
        while i < len(leftArr) and j < len(rightArr): # θ(n)

            # Compare current index element in left and right half and merge on to original array. 
            if leftArr[i] <= rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        # Merge any remaining elements in left and right halves
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i+=1
            k+=1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j+=1
            k+=1

    return arr

## TESTS ## 
print(mergesort([12, 11, 13, 5, 6, 7]))          