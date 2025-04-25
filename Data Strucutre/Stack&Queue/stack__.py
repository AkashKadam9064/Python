class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def show(self):
        return self.stack

    def peek(self):
        if self.isEmpty():
            return "Stack is empty."
        return self.stack[-1]

    def size(self):
        return len(self.stack)

if __name__ == '__main__':
    st = Stack()
    st.push('apple')
    st.push('banana')
    st.push('cherry')
    st.push('pineapple')
    st.push('mango')

    print(f"Stack = {st.stack}")
    print(f"Size of stack is {st.size()}")
    print(f"Top most element of stack is {st.peek()}")
    st.pop()
    print(st.show())

    # [print(st.pop()) for i in range(len(st.stack)+1)]


