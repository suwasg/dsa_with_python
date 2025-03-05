"""

Shell Sort is an efficient sorting algorithm that is a generalization of Insertion Sort. It works by sorting elements that are far apart from each other and progressively reducing the gap between them. This allows elements to move to their correct positions faster than in a simple insertion sort.

Key Concept
It starts by sorting elements that are far apart from each other.
It gradually reduces the gap between elements to be compared.
It uses insertion sort on each sub-array formed by the gap.

SHELL_SORT(A)
1. N ← length(A)
2. gap ← N / 2
3. while gap > 0 do
4.     for i ← gap to N-1 do
5.         temp ← A[i]
6.         j ← i
7.         while j ≥ gap and A[j - gap] > temp do
8.             A[j] ← A[j - gap]
9.             j ← j - gap
10.         A[j] ← temp
11.     gap ← gap / 2
12. return A

"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initial gap

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap

# Example usage
arr = [12, 34, 54, 2, 3]
arr2 = [12, 34, 54, 2, 3, 1, 9, 10]
shell_sort(arr)
shell_sort(arr2)
print("Sorted Array:", arr)
print("Sorted Array:", arr2)
