def binary_search(arr, target):
    if not arr:
        return False
    mid = int(len(arr)/2)
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr[mid + 1: ], target)
    else:
        return binary_search(arr[ :mid], target)
    return False

sorted_array = [10,20,30,40,50]
target = 40
print(binary_search(sorted_array, target))