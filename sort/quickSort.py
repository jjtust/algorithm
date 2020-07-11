def quickSort(arr, left, right):
    """快速排序实现"""
    
    # 时间复杂度：O(nlogn)
    # 空间复杂度：O(1)
    
    if left >= right:
        return
    
    key = arr[left]
    low = left
    high = right
    
    while low < high:
        while low < high and arr[high] > key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < key:
            low += 1
        arr[high] = arr[low]
    arr[high] = key
    
    quickSort(arr, left, low-1)
    quickSort(arr, high+1, right)
