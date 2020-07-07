def findKthLargest(nums, k):
    """数组中的第K最大元素"""
    # 时间复杂度：O(nlong)
    nums.sort(reverse=True)
    return nums[k-1]

import random

def findKthLargest(nums, k):
    """数组中的第K最大元素"""
    # 时间复杂度：O(n)
    random_num = random.choice(nums)
    # (k...)
    larger_nums = [i for i in nums if i > random_num]
    # (...k)
    less_nums = [i for i in nums if i < random_num]
    # 
    if len(larger_nums) <= k-1 and len(less_nums) <= len(nums)-k:
        return random_num
    elif len(larger_nums) >= k:
        return findKthLargest(larger_nums, k)
    else:
        return findKthLargest(less_nums, k-len(nums)+len(less_nums))

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
