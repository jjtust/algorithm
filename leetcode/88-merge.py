def merge(nums1, m, nums2, n):
    """将nums2合并到nums1中，使nums1成为一个有序数组"""
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    new_nums = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            new_nums.append(nums1[i])
            i += 1
        else:
            new_nums.append(nums2[j])
            j += 1
    new_nums += nums1[i:m]
    new_nums += nums2[j:n]
    for index, value in enumerate(new_nums):
        nums1[index] = value
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
