import random

random_list = [random.randint(1,9) for _ in range(10)]

print("Before sorting")
print(random_list)

def bubble_sort(arr):
    n = len(arr)
    if n == 0:
        return "no elements in list"
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_list = bubble_sort(random_list)
print("Sorted list:")
print(sorted_list)
