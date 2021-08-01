def fibo(n):
    cache = [0 for i in range(n + 1)]  # n+1개
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

def fibo_r(n):
    if n == 1:
        return 1
    return fibo_r(n-1) + n
print(fibo_r(100))
print(fibo(100))