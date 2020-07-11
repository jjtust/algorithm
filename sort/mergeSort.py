def _merge(left, right):
    """将左右两个已排好序的列表合并"""
    res = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res += left[i:]
    res += right[j:]
    return res
    
# O(nlogn)
def merge_sort(arr):
    """归并排序实现"""
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    # 将左半边排序
    left = merge_sort(arr[:mid])
    # 将右半边排序
    right = merge_sort(arr[mid:])
    # 将已排好序的左右子序列合并成一个序列
    res = _merge(left, right)
    
    return res
    
merge_sort([1, 2, 5, 3, 4])
