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


def sortColors(nums):
    """使用三路快速排序算法进行排序"""
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    # 遍历一遍
    zero = -1 # [0...zero] == 0
    two = len(nums) # [two...n-1] == 2
    i = 0 # [zero+1...two-1] == 1
    
    while i < two:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            nums[zero+1], nums[i] = nums[i], nums[zero+1]
            zero += 1
            i += 1
        else:
            assert nums[i] == 2
            nums[i], nums[two-1] = nums[two-1], nums[i]
            two -= 1
    
        
        
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
