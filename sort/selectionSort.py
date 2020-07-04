# O(n^2)
def selection_sort(arr):
    """选择排序实现"""
    size = len(arr)
    for i in range(size):
        largest_index = i
        for j in range(i+1, size):
            if arr[j] < arr[largest_index]:
                largest_index = j
        arr[largest_index], arr[i] = arr[i], arr[largest_index]
    return arr

selection_sort([1, 3, 2])
