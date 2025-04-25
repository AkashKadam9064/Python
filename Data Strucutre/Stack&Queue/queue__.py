class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def show(self):
        return self.queue

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.queue[0]

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    st = Queue()
    print(st.show(), f"{st.dequeue()}")

    st.enqueue('apple')
    st.enqueue('mango')
    st.enqueue('banana')

    print(st.queue)
    print(f"Size of queue is {st.size()}")
    print(f"First element of queue is {st.peek()}")
    print(f"{st.dequeue()}")





