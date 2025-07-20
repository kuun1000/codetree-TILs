class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        
        self.head = new_node
        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        
        self.tail = new_node
        self.node_num += 1

    def pop_front(self):
        if self.head is None:
            print(-1)
        else:
            temp = self.head
            print(temp.data)
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.node_num -= 1

    def pop_back(self):
        if self.tail is None:
            print(-1)
        else:
            temp = self.tail
            print(temp.data)
            self.tail = temp.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            self.node_num -= 1

    def size(self):
        print(self.node_num)

    def empty(self):
        print(1 if self.node_num == 0 else 0)

    def front(self):
        if self.head is None:
            print(-1)
        else:
            print(self.head.data)

    def back(self):
        if self.tail is None:
            print(-1)
        else:
            print(self.tail.data)



n = int(input())
linkedList = DoubleLinkedList()

for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        linkedList.push_front(int(command[1]))
    elif command[0] == 'push_back':
        linkedList.push_back(int(command[1]))
    elif command[0] == 'pop_front':
        linkedList.pop_front()
    elif command[0] == 'pop_back':
        linkedList.pop_back()
    elif command[0] == 'size':
        linkedList.size()
    elif command[0] == 'empty':
        linkedList.empty()
    elif command[0] == 'front':
        linkedList.front()
    elif command[0] == 'back':
        linkedList.back()