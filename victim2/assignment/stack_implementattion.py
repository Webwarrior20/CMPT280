class Stack:
    def __init__(self):
        self.items = []

    def push(self, v):
        self.items.append(v)

    def pop(self):
        return self.items.pop()

s = Stack()
s.push(3)
s.push(7)
print(s.pop())
