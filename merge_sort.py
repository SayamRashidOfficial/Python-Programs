def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_ptr, right_ptr = 0, 0

    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] < right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1

    result.extend(left[left_ptr:])
    result.extend(right[right_ptr:])
    return result

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)

print("Given array is:", arr)
print("Sorted array is:", sorted_arr)










def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_ptr, right_ptr = 0, 0

    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] < right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1

    # Append any remaining elements
    result.extend(left[left_ptr:])
    result.extend(right[right_ptr:])
    return result

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)

print("Given array is:", arr)
print("Sorted array is:", sorted_arr)




