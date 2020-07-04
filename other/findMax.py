# O(n)
def find_max(arr):
    """返回列表中的最大值"""
    assert len(arr) > 0, "the size of array must larger than 0"
    max_val = arr[0]
    for value in arr[1:]:
        if value > max_val:
            max_val = value
    return max_val
   
if __name__ == "__main__":
    findMax([1, -1])
