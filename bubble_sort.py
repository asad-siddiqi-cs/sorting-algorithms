# implementation of the bubble sort algorithm on a randomly generated list

import random

# Generating a list of length 10 with random values between 1 and 9
random_list = [random.randint(1,9) for _ in range(10)]



print("Before sorting")
print(random_list)

def bubble_sort(arr):
    
    """
    Bubble sort algorithm

    Time complexity:
    - Best case: O(n)
    - Average case: O(n^2)
    - Worst case: O(n^2)
    
    Space comlexity:
    - O(1)
    """

    n = len(arr)
    # if the list is empty return this message
    if n == 0:
        return []
    for i in range(n): # O(n)
        # set a variable to keep track whenever a swap is to be made
        swapped = False
        for j in range(n - i - 1): # O(n)
            if arr[j] > arr[j + 1]:
                # swap current element in array with the next element
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        # if no swap is made, stop the loop and finish searching, used for optimisation
        if not swapped:
            break
    return arr

# total time complexity of algorithm - 
# O(n^2) - Worst Case
# if the list is already sorted, best case for bubble sort would then be O(n)

sorted_list = bubble_sort(random_list)
print("Sorted list:")
print(sorted_list)
