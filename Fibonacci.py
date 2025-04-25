def rec_fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return rec_fib(num - 1) + rec_fib(num - 2)

def fib_series(num):
    if num < 0:
        return "Negative Value"
    n1, n2 = 0, 1
    print(n1)
    print(n2)

    for i in range(num):
        temp = n1 + n2
        print(temp)
        n1, n2 = n2, temp

if __name__ == '__main__':
    print(fib_series(10))
    # print(rec_fib(11))