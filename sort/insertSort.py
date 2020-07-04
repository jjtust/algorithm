class InsertSort:
    @staticmethod
    def insert_sort(arr):
        n = len(arr)
        for i in range(1, n):
            # current value
            tmp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > tmp:
                # move the big last value to next
                arr[j+1] = arr[j]
                j -= 1
            # put current value into the right position
            arr[j+1] = tmp


if __name__ == "__main__":
    a = [3, 2, 1]
    InsertSort.insert_sort(a)
    print(a)
