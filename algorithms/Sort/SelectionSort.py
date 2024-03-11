''' Going from left to right, select an element and compare it with all the other elements on the right.
After finding the smallest element on the right, swap it. '''

# Selection Sort for simple datasets - easy to understand
# Time Complexity: O(n^2)
# Space Complexity: O(1) - Temp Variable to store min element index


def selectionsort(arr):
    for i in range(len(arr)): #(O(n))

        # Initialize the minimum element to the first index
        minElementIndex = i

        # Loop through the adjacent elements from the selected element
        for j in range(i+1, len(arr)): #(O(n))
            if arr[j] < arr[minElementIndex]:
                minElementIndex = j

        # Swap the elements and continue to run the loop
        arr[i], arr[minElementIndex] = arr[minElementIndex], arr[i]
    
    return arr
            
## TESTS ##
print(selectionsort([64, 25, 12, 22, 11]))