def linear_search(num):
    l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(0, len(l)):
        if l[i] == num:
            return i
    return -1
print("The number index is", linear_search(1000))

