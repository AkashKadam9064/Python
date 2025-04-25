class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def find_min(self):
        min = self.head.data
        while self.head:
            if min >= self.head.data:
                min = self.head.data
            self.head = self.head.next
        return min

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            return self.insert_at_beginning(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data, None)

    def insert_values(self, data_list):
        for i, data in enumerate(data_list):
            self.insert_at_end(data)
        return

    def get_length(self):
        count = 0
        while self.head:
            self.head = self.head.next
            count += 1
        return count

    def insert_at(self, index, element):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(element)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([10, 34, 40, 30, 23, 55, 66])
    # ll.traversal()
    ll.insert_at(0, 1)
    ll.traversal()
    

























































