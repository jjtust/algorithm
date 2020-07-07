def twoSum(numbers, target):
    """给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。"""
    # 暴力破解法 O(n^2)
    i = 0
    j = 0
    # 第一层循环
    while i < len(numbers):
        j = i + 1
        # 第二层循环
        while j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            j += 1
        i += 1   


def binarySearch(numbers, target):
    # 二分搜索法
    # 在[l...r]范围内寻找target
    l = 0
    r = len(numbers) - 1
    # l == r，对于[l...r]依然是有效的
    while l <= r:
        mid = (l + r) // 2
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            # target在[l...mid-1]中
            r = mid - 1
        else:
            # target在[mid+1...r]中
            l = mid + 1
    return -1


def twoSum(numbers, target):
    """给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。"""
    # 时间复杂度：O(nlogn)
    # 在[i...len(numbers)-1)中寻找target的第一个元素
    i = 0
    # 一层循环
    while i < len(numbers) - 1:
        # 在[i+1, len(numbers)-1]中寻找target的第二个元素
        index2 = binarySearch(numbers[0:i] + numbers[i + 1:], target - numbers[i])
        if index2 != -1:
            # 返回的下标识从1开始，前一个元素已经被删除了
            return [i + 1, index2 + 2]
        i += 1
    return None

def twoSum(numbers, target):
    """给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。"""
    # 对撞指针
    # 时间复杂度O(n)
    assert len(numbers) >= 2
    # 在[l...r]中寻找target的两个索引值
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    raise Exceptioon("The input has no solutions.")

numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))
