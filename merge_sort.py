"""
What is Merge Sort?
Merge Sort is a divide-and-conquer sorting algorithm that recursively:

Divides the array into two halves.
Sorts each half.
Merges the two sorted halves back together.

✅ Best Used For:
Sorting large datasets efficiently.
External sorting (Sorting large files stored in disk/memory).
Sorting linked lists (due to efficient merging).

PSEUDOCODE:
MERGE_SORT(A, left, right)
1. If left < right:
2.     mid = (left + right) / 2
3.     MERGE_SORT(A, left, mid)
4.     MERGE_SORT(A, mid+1, right)
5.     MERGE(A, left, mid, right)

"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example Usage
arr = [6, 3, 8, 5, 2, 7, 4, 1]
merge_sort(arr)
print("Sorted Array:", arr)
