def removeDuplicates(nums):
    if not nums:
        return 0
    nums.sort()
    k = nums[0]
    # 遍历所有元素，保证每个元素只出现一次
    for element in nums[1:]:
        if element != k:
            k = element
        else:
            nums.remove(k)
    return len(nums)

print(removeDuplicates([1,1,2,2]))
