"""
Bubble Sort is one of the simplest sorting algorithms that repeatedly swaps adjacent elements if they are in the wrong order. This process continues until the entire list is sorted.

How Bubble Sort Works?
i. Start from the first element of the array.
ii. Compare the current element with the next one.
iii. If the current element is greater than the next one, swap them.
iv. Move to the next adjacent pair and repeat steps ii-iii for the entire array.
v. The largest element moves to the last position at the end of each full pass.
vi. Repeat the process for the remaining (unsorted) elements until no swaps are needed.

PSEUDOCODE: 
BUBBLE_SORT(A)
1. N ← length(A)
2. for i ← 0 to N - 1 do
3.     swapped ← false
4.     for j ← 0 to N - i - 2 do
5.         if A[j] > A[j + 1] then
6.             swap(A[j], A[j + 1])
7.             swapped ← true
8.     if swapped = false then
9.         break
10. return A

"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Number of passes/comparisions
        swapped = False
        for j in range(n - i - 1):  # Traverse unsorted part
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if needed
                swapped = True
        if not swapped:  # If no swaps, array is already sorted
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted Array:", sorted_arr)


"""
NOTE: Time Complexity:
Best Case (Already Sorted): O(N)
Worst & Average Case: O(N²) (when the array is in reverse order)
Space Complexity: O(1) (In-place sorting)

NOTE: Use Cases of Bubble Sort in Daily Life
Although Bubble Sort is not the most efficient algorithm, it is still used in:
Teaching Sorting Concepts:
It helps beginners understand the fundamentals of sorting.

Small Datasets Sorting:
When the dataset is small, Bubble Sort performs adequately.

Nearly Sorted Data Optimization:
It is efficient in cases where only a few elements are misplaced.

Detecting Sorted Data:
The early stopping mechanism helps check if data is already sorted.

Animation and Visualization in Education:
Used in animation-based learning tools to demonstrate sorting techniques.

NOTE: When to Avoid Bubble Sort?
When working with large datasets, as its O(N²) complexity makes it very slow.
When performance is critical, prefer Quick Sort, Merge Sort, or Heap Sort.
"""