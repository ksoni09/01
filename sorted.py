import random

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]

print("Original List:", random_list)

# Sort the list using bubble sort
bubble_sort(random_list)

print("Sorted List:", random_list)