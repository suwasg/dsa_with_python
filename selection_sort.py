"""

Selection Sort is a simple and intuitive sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion and moves it to the correct position.

Key Concept
Find the minimum (or maximum) element from the unsorted portion.
Swap it with the first element of the unsorted portion.
Expand the sorted portion and repeat until the list is sorted.

SELECTION_SORT(A)
1. N ← length(A)
2. for i ← 0 to N-1 do
3.     min_index ← i
4.     for j ← i+1 to N-1 do
5.         if A[j] < A[min_index] then
6.             min_index ← j
7.     swap(A[i], A[min_index])
8. return A

"""



def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 9]
arr1 = [6, 3, 25, 12, 22, 11, 99]
selection_sort(arr)
selection_sort(arr1)
print("Selection Sorted Array:", arr)
print("Selection Sorted Array1:", arr1)