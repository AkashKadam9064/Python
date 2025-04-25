import threading
import time

x = 1
lock = threading.Lock()
def str1():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(0.5)
    lock.release()

def str2():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(0.5)
    lock.release()

t2 = threading.Thread(target=str2)
t1 = threading.Thread(target=str1)

t1.start()
t2.start()
