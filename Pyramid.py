def pyramid(num):
    for i in range(num, 1, -1):
        if i == 2:
            break
        [print(j, end=' ')for j in range(1, i)]
        print()

    for i in range(1, num):
        [print(j, end=' ') for j in range(1, i+1)]
        print()

pyramid(6)

