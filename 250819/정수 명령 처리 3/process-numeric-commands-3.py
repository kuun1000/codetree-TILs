from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
    comm = input().split()

    if comm[0] == 'push_front':
        dq.appendleft(comm[1])
    elif comm[0] == 'push_back':
        dq.append(comm[1])
    elif comm[0] == 'pop_front':
        print(dq.popleft())
    elif comm[0] == 'pop_back':
        print(dq.pop())
    elif comm[0] == 'size':
        print(len(dq))
    elif comm[0] == 'empty':
        print(1 if not dq else 0)
    elif comm[0] == 'front':
        print(dq[0])
    else:
        print(dq[-1])