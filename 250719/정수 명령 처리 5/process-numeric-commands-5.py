n = int(input())
arr = []

for _ in range(n):
    line = input().split()
    command = line[0] 
    
    if command == 'push_back':
        arr.append(line[1])
    elif command == 'pop_back':
        arr.pop()
    elif command == 'size':
        print(len(arr))
    elif command == 'get':
        print(arr[int(line[1])-1])