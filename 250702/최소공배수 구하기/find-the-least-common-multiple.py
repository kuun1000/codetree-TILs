n, m = map(int, input().split())

# Please write your code here.
def get_GCD(n, m):
    while m:
        n, m = m, n % m
    return n

def get_LCM(n, m):
    return (n * m) // get_GCD(n, m)

print(get_LCM(n, m))