def main():
    """数据规模测试"""
    for i in range(10, 23):
        n = pow(2, i)
        arr = generate_random_array(0, 10**8, n)
        print("data size 2^%d = %d" % (i, n))
        %time merge_sort(arr)
main()
