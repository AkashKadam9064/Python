def shell_sort(arr):

    size = len(arr)
    gap = size//2
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    elements = [10, 24,  60,8588, 345656, 322, 28477, 59, 66, 43, 32, 5, 33, 45, 0]
    shell_sort(elements)
    print(elements)