def reverse(s):
    """反转字符串"""
    size = len(s)
    new_s = [i for i in range(size)]
    for i in range(size // 2 + 1):
        new_s[i], new_s[size-i-1] = s[size-i-1], s[i]
    s_str = "".join(new_s)
    return s_str
    
def int_to_string(num):
    """将整形数字转换成字符串"""
    if num == 0:
        return "0"
    if num < 0:
        is_negative_num = True
        num = -num
    else:
        is_negative_num = False
    s = ""
    while num:
        s += str(num % 10)
        num = num // 10
    s = reverse(s)
    if is_negative_num:
        s = "-" + s
    return s
    
if __name__ == "__main__":
    int_to_string(11234)
