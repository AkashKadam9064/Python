def swap(a, b, list):
    list[a], list[b] = list[b], list[a]

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while end > 0 and arr[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, arr)
    swap(pivot_index, end, arr)

    return end

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)


if __name__ == '__main__':
    elements = [5, 1, 8, 7, 9, 6, 2, 3, 4]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
