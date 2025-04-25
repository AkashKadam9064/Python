def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    else:
        return "Prime"

def prime_upto_num(n):
    a = []
    for num in range(2, n+1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            a.append(num)
        num += 1
    return len(a)

def prime_upto_nth_term(nth):
    count = 0
    num = 2
    a = []
    while count < nth:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            a.append(num)
            count += 1
        num += 1
    return a

if __name__ == '__main__':
    # print(prime(100))
    print(prime_upto_nth_term(100))
    # print(prime_upto_num(100))

