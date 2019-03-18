def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1


arr = list(range(10))
start = 0
end = len(arr) - 1
target = 10

print(binary_search(arr,start, end, target))