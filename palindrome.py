def is_palindrome(s):
    b = ""
    for i in s:
        if i.isalnum():
            b = b + i.lower()
    if b == b[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome("Mala1y1alam?"))

