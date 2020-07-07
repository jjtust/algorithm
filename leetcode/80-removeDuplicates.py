def removeDuplicates(nums):
    """给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度"""
    if not nums:
        return 0
    num_count = {nums[0]: 1}
    # 遍历所有元素，保证每个元素只出现2次
    for element in nums[1:]:
        count = num_count.get(element, 0)
        if count < 2:
            num_count[element] = count + 1
        else:
            nums.remove(element)
    return len(nums)

nums = [1,1,1,2,2,3]
k = removeDuplicates(nums)
print(k)
print(nums)
