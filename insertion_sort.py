"""

Insertion Sort is a simple and efficient sorting algorithm that works similarly to how we sort playing cards in our hands. It is based on the idea of building a sorted array one element at a time by picking elements and placing them in their correct position.

Key Concept
It takes one element at a time and compares it with previously sorted elements.
It shifts larger elements to the right and inserts the selected element at the correct position.
Best for small or nearly sorted data sets.

INSERTION_SORT(A)
1. for i ← 1 to length(A) - 1 do
2.     key ← A[i]
3.     j ← i - 1
4.     while j ≥ 0 and A[j] > key do
5.         A[j + 1] ← A[j]  // Shift elements to the right
6.         j ← j - 1
7.     A[j + 1] ← key  // Insert the key element
8. return A


"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr  # Return the sorted array

# Example usage
arr = [12, 11, 13, 5, 6]
arr2 = [5, 3, 8, 4, 2]
sorted_arr = insertion_sort(arr)
sorted_arr2 = insertion_sort(arr2)
print("Sorted Array:", sorted_arr)
print("Sorted Array:", sorted_arr2)