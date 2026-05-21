# implementation of quicksort algorithm on a randomly generated unsorted list

import random

# Generating a list of length 10 with random values between 1 and 9
random_list = [random.randint(1,9) for _ in range(10)]

print("Before sorting")
print(random_list)


def quick_sort(arr):
    """
    Quick sort algorithm

    Time complexity:
    - Best case: O(nlogn)
    - Average case: O(nlogn)
    - Worst case: O(n^2)
    
    Space complexity:
    - O(logn)
    - o(n)
    """

    # base case of recursion
    if len(arr) < 2:
        return arr

    # randomly choosing a reference value from the list
    pivot = random.choice(arr)

    less, equal, greater = [],[],[]

    # checking whether each element is less than, equal or greater than the reference value
    for elt in arr:
        if elt < pivot:
            less.append(elt)
        elif elt == pivot:
            equal.append(elt)
        else:
            greater.append(elt)

    # recursiveley calling quicksort to sort the list
    return quick_sort(less) + equal + quick_sort(greater)

sorted_list = quick_sort(random_list)

print("After sorting:")
print(sorted_list)

"""
Quick sort is significantly faster than bubble sort
 for large datasets because it partitions the list recursively, 
 achieving an average time complexity of O(nlogn) 
 compared to bubble sorts O(n^2).
"""