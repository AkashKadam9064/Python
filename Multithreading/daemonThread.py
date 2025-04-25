import threading
import time

file = "demo.txt"
text = " "
def readfile():
    global file, text
    while True:
        with open("demo.txt", 'r') as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for i in range(20):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readfile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()