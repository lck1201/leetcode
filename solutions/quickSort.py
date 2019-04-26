import random

def partition(nums, left, right):
    pivotIdx = random.randint(left, right)
    nums[pivotIdx], nums[right] = nums[right], nums[pivotIdx]
    pivotVal = nums[right]

    partitionIndex = left
    for i in range(left, right):
        if nums[i] < pivotVal:
            nums[i], nums[partitionIndex] = nums[partitionIndex], nums[i]
            partitionIndex += 1

    nums[right], nums[partitionIndex] = nums[partitionIndex], nums[right]
    return partitionIndex

def quicksort(nums, left, right):
    if right > left:
        partitionIndex = partition(nums, left, right)
        quicksort(nums, left, partitionIndex - 1)
        quicksort(nums, partitionIndex + 1, right)

nums = [-3, 6, 3, 9, 4, 2, 8, 66, 4, 2, 90, -6, 3, 2]
quicksort(nums, 0, len(nums) - 1)
print(nums)
