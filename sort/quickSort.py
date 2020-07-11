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
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[high] = key
    
    quickSort(arr, left, low-1)
    quickSort(arr, high+1, right)
    

def quickSort(ary):
    return _quick_sort(ary, 0, len(ary)-1)

def _quick_sort(ary, left, right):
    if left >= right: return ary
    key = ary[left]  # 每次都选最左边为key
    lp = left
    rp = right
    while (lp < rp):
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[left]  # 这里不能用key，是交换数组内数字
    _quick_sort(ary, left, lp-1)
    _quick_sort(ary, lp+1, right)  # 这里lp, rp永远是相等的。所以都可以。
    return ary    
    
def quickSort(arr):
    """快速排序实现"""
    
    if len(arr) < 2:
        return arr
    
    key = arr[0]
    low = [i for i in arr if i < key]
    high = [i for i in arr if i > key]
    middle = [i for i in arr if i == key]
    return quickSort(low) + middle + quickSort(high)
        
arr = [random.randint(0, 10**4) for i in range(10**5)]
arr = quickSort(arr)
for index in range(len(arr)-1):
    if arr[index] > arr[index+1]:
        raise Exception("sort error")
