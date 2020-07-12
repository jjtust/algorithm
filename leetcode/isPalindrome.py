def isPalindrome(s):
    """给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    
    # 对撞指针
    # 空字符串属于回文串
    if not str:
        return True
    
    # 头指针，尾指针，首尾相同
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
        
    return True
    
    
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
print(isPalindrome(s))
