def reverseString(s):
    """将输入的字符串反转过来"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    # 对撞指针
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
        
s = ["h","e","l","l","o"]
reverseString(s)
print(s)
