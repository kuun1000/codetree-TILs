a = list(input())
length = len(a)

max_val = 0
for i in range(length):
    a[i] = str(1- int(a[i]))
    num = int('0b'+''.join(a), 2)
    
    max_val = max(max_val, num)
    
    a[i] = str(1- int(a[i]))

print(max_val)