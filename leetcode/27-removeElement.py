def removeElement(nums, val):
    """原地移除所有数值等于 val 的元素，并返回移除后数组的新长度"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    if not nums:
        return 0
        
    # [0...k)存放非val元素
    k = 0 
    # 遍历所有元素，保证所有非val元素都按顺序存在[0...k)中
    for element in nums:
        if element != val:
            nums[k] = element
            k += 1
    return k

def removeElement(nums, val):
    """原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    if not nums:
        return 0
    length = len(nums)
    # 计算val出现的次数
    val_count = nums.count(val)
    
    # 删除val，一共执行val_count次
    for i in range(val_count):
        nums.remove(val)
        
    return length - val_count

nums = [3, 2, 2, 3]
k = removeElement(nums, 3)
print(k)
print(nums[:k])
