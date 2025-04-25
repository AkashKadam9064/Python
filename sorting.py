def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1 -i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

def selection_sort(num):
    size = len(num)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if num[min] > num[j]:
                min = j
        num[i], num[min] = num[min], num[i]
    return num

def insertion_sort(num):
    for i in range(1, len(num)):
        anchor = num[i]
        j = i - 1
        while j >= 0 and num[j] > anchor:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = anchor
    return num

def quick_sort(num):
    pass

def merge_sort(num):
    pass

if __name__ == '__main__':
    list = [10, 30, 20, 90, 70, 80, 100, 40, 60, 50, 0, 0, 0, 10, 20]
    print(insertion_sort(list))
