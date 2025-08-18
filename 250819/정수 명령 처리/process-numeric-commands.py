class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return int(not self.items)

    def pop(self):
        if not self.empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if not self.empty():
            return self.items[-1]

n = int(input())

s = Stack()
for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        s.push(int(command[1]))
    elif command[0] == 'pop':
        print(s.pop())
    elif command[0] == 'size':
       print(s.size()) 
    elif command[0] == 'empty':
        print(s.empty())
    else:
        print(s.top())
