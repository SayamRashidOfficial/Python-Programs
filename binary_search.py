def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1


sorted_list = [3, 4, 5, 6, 7, 8, 9]
element_to_find = 4
result = binary_search(sorted_list, element_to_find)

if result != -1:
    print(f"Element {element_to_find} found at index {result}")
else:
    print(f"Element {element_to_find} not found")
