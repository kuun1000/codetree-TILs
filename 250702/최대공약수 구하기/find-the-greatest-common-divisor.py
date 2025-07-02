n, m = map(int, input().split())

# Please write your code here.
def get_GCD(n, m):
    while m:
        n, m = m, n % m
    return n

print(get_GCD(n, m))