# O(logn)
def binary_search(arr, target):
    """二分搜索法实现"""
    
    # 在[l...r]范围内寻找target  (明确变量的定义)
    l = 0
    r = len(arr) - 1
    
    # 当l == r时，区间[l...r]依然有效  (循环不变量)
    while l <= r:
        
        mid = (l + r) // 2
        
        if arr[mid] == target:
            return mid
        # target在[mid+1...r]中
        elif arr[mid] < target:
            l = mid + 1
        # target在[l...mid-1]中
        else:
            r = mid - 1
    
    # 找不到target返回-1
    return -1


def binary_search(arr, target):
    """二分搜索法实现"""
    
    # 在[l...r)范围内寻找target
    l = 0
    r = len(arr)
    
    # 当l == r时，区间[l...r)是无效的
    while l < r:
        
        mid = (l + r) // 2
        
        if arr[mid] == target:
            return mid
        # target在[mid+1...r)中
        elif arr[mid] < target:
            l = mid + 1
        # target在[l...mid)中
        else:
            r = mid
    
    # 找不到target返回-1
    return -1


def main():
    """数据规模测试"""
    for i in range(10, 28):
        n = pow(2, i)
        arr = generate_random_array(0, 10**8, n)
        print("data size 2^%d = %d" % (i, n))
        %time binary_search(arr, 0)
        
        
main()

# data size 2^10 = 1024
# CPU times: user 7 µs, sys: 1 µs, total: 8 µs
# Wall time: 10 µs
# data size 2^11 = 2048
# CPU times: user 7 µs, sys: 23 µs, total: 30 µs
# Wall time: 11.2 µs
# data size 2^12 = 4096
# CPU times: user 8 µs, sys: 1 µs, total: 9 µs
# Wall time: 10 µs
# data size 2^13 = 8192
# CPU times: user 10 µs, sys: 0 ns, total: 10 µs
# Wall time: 11.9 µs
# data size 2^14 = 16384
# CPU times: user 9 µs, sys: 1e+03 ns, total: 10 µs
# Wall time: 11 µs
# data size 2^15 = 32768
# CPU times: user 10 µs, sys: 0 ns, total: 10 µs
# Wall time: 11.7 µs
# data size 2^16 = 65536
# CPU times: user 9 µs, sys: 1 µs, total: 10 µs
# Wall time: 11 µs
# data size 2^17 = 131072
# CPU times: user 9 µs, sys: 1 µs, total: 10 µs
# Wall time: 11 µs
# data size 2^18 = 262144
# CPU times: user 11 µs, sys: 1e+03 ns, total: 12 µs
# Wall time: 13.1 µs
# data size 2^19 = 524288
# CPU times: user 10 µs, sys: 0 ns, total: 10 µs
# Wall time: 12.2 µs
# data size 2^20 = 1048576
# CPU times: user 19 µs, sys: 10 µs, total: 29 µs
# Wall time: 31.9 µs
# data size 2^21 = 2097152
# CPU times: user 19 µs, sys: 9 µs, total: 28 µs
# Wall time: 28.8 µs
# data size 2^22 = 4194304
# CPU times: user 24 µs, sys: 12 µs, total: 36 µs
# Wall time: 38.1 µs
# data size 2^23 = 8388608
# CPU times: user 25 µs, sys: 12 µs, total: 37 µs
# Wall time: 39.1 µs
# data size 2^24 = 16777216
# CPU times: user 29 µs, sys: 18 µs, total: 47 µs
# Wall time: 49.8 µs
# data size 2^25 = 33554432
# CPU times: user 29 µs, sys: 16 µs, total: 45 µs
# Wall time: 48.9 µs
# data size 2^26 = 67108864
# CPU times: user 34 µs, sys: 45 µs, total: 79 µs
# Wall time: 81.8 µs
# data size 2^27 = 134217728
# CPU times: user 38 µs, sys: 26 µs, total: 64 µs
# Wall time: 67 µs
