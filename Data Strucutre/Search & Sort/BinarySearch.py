def linear_search(numbers_list, number_to_find):
    for index, elements in enumerate(numbers_list):
        if elements == number_to_find:
            return index
    return -1

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number > number_to_find:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return -1

if __name__ == '__main__':
    numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    number_to_find = 10

    num = binary_search(numbers_list, number_to_find)
    print("The index of number is:", num)