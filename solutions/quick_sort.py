def partition(nums, left, right):
    pivotVal = nums[right]
    storeIndex = left
    for i in range(left, right):
        if nums[i] < pivotVal:
            nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
            storeIndex += 1

    nums[right], nums[storeIndex] = nums[storeIndex], nums[right]
    return storeIndex


def quicksort(nums, left, right):
    if right > left:
        partitionIndex = partition(nums, left, right)
        quicksort(nums, left, partitionIndex-1)
        quicksort(nums, partitionIndex+1, right)

