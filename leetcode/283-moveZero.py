def moveZeroes(nums):
    """将数组中的所有0移动到数组的末尾，同时保证非零元素的相对顺序"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    
    # 取出所有非零元素
    non_zeroes_elements = [num for num in nums if num]
    
    # 填充非零元素
    for index in range(len(non_zeroes_elements)):
        nums[index] = non_zeroes_elements[index]
    
    # 填充剩下的零元素
    for index in range(len(non_zeroes_elements), len(nums)):
        nums[index] = 0
        
def moveZeroes(nums):
    """将数组中的所有0移动到数组的末尾，同时保证非零元素的相对顺序"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    # nums中，[0 ... k)的元素均为非零元素
    k = 0  
    # 遍历所有元素，保证所有非零元素都按顺序存在[0...k)中
    for num in nums:
        if num:
            nums[k] = num
            k += 1
    
    # 将nums中剩余的位置存为0
    for index in range(k, len(nums)):
        nums[index] = 0
        
def moveZeroes(nums):
    """将数组中的所有0移动到数组的末尾，同时保证非零元素的相对顺序"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    # nums中，[0 ... k)的元素均为非零元素
    k = 0  
    # 遍历所有元素，保证所有非零元素都按顺序存在[0...k)中
    # 同时保证[k...len(nums))为0
    for index in range(len(nums)):
        if nums[index]:
            nums[k], nums[index] = nums[index], nums[k]
            k += 1
            
def moveZeroes(nums):
    """将数组中的所有0移动到数组的末尾，同时保证非零元素的相对顺序"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    # nums中，[0 ... k)的元素均为非零元素
    k = 0  
    # 遍历所有元素，保证所有非零元素都按顺序存在[0...k)中
    # 同时保证[k...i]为0
    for index in range(len(nums)):
        if nums[index]:
            if index != k:
                nums[k], nums[index] = nums[index], nums[k]
                k += 1
            # index == k, 无需交换元素
            else:
                k += 1      
