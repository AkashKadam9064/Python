def linear_search(num_list, num):
    for i in range(len(num_list)):
        if num == num_list[i]:
            return i
    return -1

def binary_search(list, num):
    left = 0
    right = len(list)
    while left <= right:
        mid_index = (left + right) // 2
        mid_num = list[mid_index]
        if num == mid_num:
            return mid_index
        elif mid_num > num:
            right = mid_index - 1
        else:
            left = mid_index + 1
    return -1

if __name__ == '__main__':
    number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(binary_search(number_list, 10))
