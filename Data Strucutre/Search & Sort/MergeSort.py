def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge_two_sorted_array(left_arr, right_arr)

def merge_two_sorted_array(a, b):
    len_a = len(a)
    len_b = len(b)
    sorted_arr = []
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            j += 1
    while i < len_a:
        sorted_arr.append(a[i])
        i += 1
    while j < len_b:
        sorted_arr.append(b[j])
        j += 1
    return sorted_arr

if __name__ == "__main__":
    arr = [90, 20, 100, 10, 60, 40, 70, 80, 50]
    print(merge_sort(arr))
