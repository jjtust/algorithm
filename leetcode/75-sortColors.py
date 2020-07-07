def sortColors(nums):
    """对数据范围有限的数组进行排序，可以使用计数排序"""
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    color_dict = {
        0: 0,
        1: 0,
        2: 0
    }
    for i in nums:
        assert i >= 0 & i <= 2, "the number of nums must between 0 and 2."
        color_dict[i] += 1
    
    index = 0
    for color in [0, 1, 2]:
        counts = color_dict[color]
        for i in range(index, index+counts):
            nums[i] = color
        index += counts

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
