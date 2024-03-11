''' Going from left to right, for each element, compare it with adjacent element and swap if greater by iteration.
    Finally terminate if nothing to swap'''

# Bubble sort for simple datasets - Not efficient but stable
# Time Complexity : O(n^2).
# Space Complexity : O(1)

def bubblesort(arr):

    for i in range(len(arr)): #O(n)

        # Temp variable to determine if there are no swaps for a given iteration - That's when you stop sorting
        swapped = False

        for j in range(0, len(arr) - i - 1): #O(n)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if swapped == False:
            break
    return arr


## TEST ##
print(bubblesort([64, 34, 25, 12, 22, 11, 90]))