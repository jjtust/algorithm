class ShellSort:

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                self.insert_sort(arr, gap, i)
            gap //= 2

    def insert_sort(self, arr, gap, i):

        tmp = arr[i]
        j = i - gap

        while j >= 0 and arr[j] > tmp:
            arr[j+gap] = arr[j]
            j -= gap

        arr[j+gap] = tmp


if __name__ == "__main__":
    a = [8, 7, 6, 5, 4, 3, 2, 1]
    sr = ShellSort()
    sr.shell_sort(a)
    print(a)
