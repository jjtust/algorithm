# O(logn)
def binary_search(arr, num):
    """二元搜索实现"""
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == num:
            return num
        elif arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    return None
