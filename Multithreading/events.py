import threading

event = threading.Event()
def function():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Event Triggerd...")

t1 = threading.Thread(target=function)
t1.start()

x = int(input("Do you want to trigger an event? (0/1)"))
if x == 1:
    event.set()