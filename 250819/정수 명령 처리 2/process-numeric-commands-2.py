from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        if not self.empty():
            return self.dq.popleft()

    def size(self):
        return len(self.dq)
    
    def empty(self):
        return not self.dq
    
    def front(self):
        if not self.empty():
            return self.dq[0]

n = int(input())
q = Queue()
for _ in range(n):
    comm = input().split()

    if comm[0] == 'push':
        q.push(comm[1])
    elif comm[0] == 'pop':
        print(q.pop())
    elif comm[0] == 'size':
        print(q.size())
    elif comm[0] == 'empty':
        print(int(q.empty()))
    else:
        print(q.front())