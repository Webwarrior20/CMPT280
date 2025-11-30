class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    print("Head:", ll.head.data)
