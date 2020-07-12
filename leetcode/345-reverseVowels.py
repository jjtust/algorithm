def reverseVowels(s):
    """以字符串作为输入，反转该字符串中的元音字母"""
    
    # 时间复杂度：O(n)
    # 空间复杂度：O(n)
    
    # 对撞指针
    strs = list(s)
    l = 0
    r = len(s) - 1
    vowels = {"a", "e", "i", "o", "u"}
    
    while l < r:
        if strs[l].lower() not in vowels:
            l += 1
            continue
        if strs[r].lower() not in vowels:
            r -= 1
            continue
        strs[l], strs[r] = strs[r], strs[l]
        l += 1
        r -= 1
        
    return "".join(strs)

s = "hello"
print(reverseVowels(s))
