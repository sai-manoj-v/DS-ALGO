''' Going from left to right, compare 2 elements to determine smallest number. Swap the smallest number
    until it reaches place in the sorted left array '''

# Suitable for simple datasets
# Time Complexity : O(n^2)
# Space Complexity : O(n)

def insertionsort(arr):
    
    for i in range(len(arr)): #O(n)
        
        # Temp variable for storing current element
        presentElement = arr[i]

        # Index for left array
        j = i - 1

        # Looping through the left array, shifting larger elements by one step, to swap present element in its place on sorted array. 
        while j >= 0 and presentElement < arr[j]: # O(n)
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = presentElement

    return arr

print(insertionsort([12, 11, 13, 5, 6]))