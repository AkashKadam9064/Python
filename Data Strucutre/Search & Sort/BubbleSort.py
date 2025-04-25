def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        for j in range(size - 1 - i):
            # swapped = False
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                # swapped = True
        # if not swapped:
            # break

if __name__ == '__main__':
    element = [10, 20, 90, 20, 60, 20, 30, 100, 70, 40, 0]

    bubble_sort(element)
    print(element)

