def merge(arr1, arr2):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    result.extend(arr1 or arr2)
    return result

def mergeSort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    leftArr = array[:mid]
    rightArr = array[mid:]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    return merge(leftArr, rightArr)


x = [3, 2, 1,6,8,4,3,88,4,2,2,2,234,47,24,894]
print(mergeSort(x))
