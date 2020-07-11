# O(n^2)
def selection_sort(arr):
    """选择排序实现"""
    
    size = len(arr)
    
    # 第一层循环[i...size)
    for i in range(size):
        lowerest_index = i
        
        # 第二层循环[i+1...size)
        for j in range(i+1, size):
            # 寻找最小值
            if arr[j] < arr[lowerest_index]:
                lowerest_index = j
                
        # 不断将最小值移动到最左边
        arr[lowerest_index], arr[i] = arr[i], arr[lowerest_index]
    return arr

selection_sort([1, 3, 2])
