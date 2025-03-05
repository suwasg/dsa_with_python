""""

Radix Sort is a non-comparative sorting algorithm that sorts numbers digit by digit. It processes numbers from the least significant digit (LSD) to the most significant digit (MSD) or vice versa. Since it doesn’t compare elements directly, it can be faster than QuickSort or MergeSort for specific datasets.

✅ Best Used For:
Sorting large numbers efficiently
Sorting fixed-width integers (like phone numbers, ZIP codes)

How Radix Sort Works?
Radix Sort sorts numbers by placing them into buckets based on the value of each digit, starting from the least significant digit (LSD). It uses counting sort as a subroutine for sorting digits.

RADIX_SORT(A, d)
1. for i ← 0 to d-1 do
2.     Apply a stable sorting algorithm (like Counting Sort) on digit i
3. return A


"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count array to store position of each digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output back to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)  # Get maximum number
    exp = 1  # Start with 1s place

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to next place value

# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr2 = [170, 945, 725, 1, 82, 24, 20, 6]
radix_sort(arr)
radix_sort(arr2)
print("Sorted Array:", arr)
print("Sorted Array:", arr2)
