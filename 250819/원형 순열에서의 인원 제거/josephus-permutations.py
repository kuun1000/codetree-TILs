from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if not self.empty():
            return self.dq.popleft()

    def front(self):
        if not self.empty():
            return self.dq[0]

n, k = list(map(int, input().split()))

q = Queue()
for i in range(1, n+1):
    q.push(i)

while q.size() != 1:
    for i in range(1, k):
        q.push(q.front())
        q.pop()
    print(q.front(), end=" ")
    q.pop()
    
print(q.front(), end=" ")