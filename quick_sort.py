"""
What is Quick Sort?
Quick Sort is also a divide-and-conquer algorithm, but instead of merging sorted subarrays, it:

Chooses a pivot.
Partitions the array into elements less than and greater than the pivot.
Recursively sorts the partitions.

✅ Best Used For:
Sorting large datasets efficiently.
In-place sorting (less memory than Merge Sort).
Competitive programming (Quickest on average).

QUICK_SORT(A, low, high)
1. if low < high:
2.     pivot = PARTITION(A, low, high)
3.     QUICK_SORT(A, low, pivot-1)
4.     QUICK_SORT(A, pivot+1, high)


"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  
        quick_sort(arr, low, pivot_index - 1)  
        quick_sort(arr, pivot_index + 1, high)  

# Example Usage
arr = [6, 3, 8, 5, 2, 7, 4, 1]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)