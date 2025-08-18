class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items

    def pop(self):
        if not self.empty():
            return self.items.pop()
    
    def top(self):
        if not self.empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

arr = input()
s = Stack()
ok = True

for elem in arr:
    if elem == '(':
        s.push(elem)
    else:
        if s.empty():
            ok = False
            break
        s.pop()

if ok and s.empty():
    print('Yes')
else:
    print('No')