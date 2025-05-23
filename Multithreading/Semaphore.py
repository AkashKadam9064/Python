import threading
import time

semaphore = threading.BoundedSemaphore(value=5)
def access(thread_number):
    print(thread_number, "is trying to access!")
    semaphore.acquire()
    print(thread_number, "granted access!")
    time.sleep(5)
    print(thread_number, "is releasing!")
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()