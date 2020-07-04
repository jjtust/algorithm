def generate_random_array(rangeL, rangeR, n):
    """生成一个随机数组"""
    assert n > 0, "the size of array must larger than 0"
    assert rangeL <= rangeR, "rangeL must be less than rangeR"
    arr = [random.randint(rangeL, rangeR) for i in range(n)]
    return arr
