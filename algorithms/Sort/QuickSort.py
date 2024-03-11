def partition(arr, low, high):

    # Finding pivot index using median
    midIndex = medianIndex = (low + high) // 2
    if arr[midIndex] <= arr[low] <= arr[high]:
        medianIndex = low
    elif arr[low] <= arr[high] <= arr[midIndex]:
        medianIndex = high
    else:
    # Handle the case where two or all elements are equal (unlikely)
        medianIndex = midIndex
    
    # Swapping the highest with median index
    arr[medianIndex], arr[high] = arr[high], arr[medianIndex]

    # Initializing the low index for swap tracker
    i = low - 1

    for j in range(low, high):

        # If the element is greater than the pivot, increase the i index and swap it with current large number
        if arr[j] <= arr[high]:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    # Finally swap the pivot to its right position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the next pivot element
    return i + 1

def quicksort(arr, low = 0, high = -1):

    high  = len(arr) - 1 if high == -1 else high    
    
    if low < high: 
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)

    return arr


## TESTS ## 
print(quicksort([10, 7, 8, 9, 1, 5]))