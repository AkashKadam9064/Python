def insertion_sort(elements):

    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor

if __name__ == '__main__':
    element = [34, 10, 56, 90, 56, 11, 21, 32, 99, 1]
    insertion_sort(element)
    print(element)