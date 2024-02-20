import random

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive calls to merge_sort for both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the two sorted halves
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any elements are left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Generate a random list of numbers
random_list = [random.randint(1, 100) for _ in range(10)]

print("Original List:", random_list)

# Sort the list using merge sort
merge_sort(random_list)

print("Sorted List:", random_list)