n, m = map(int, input().split())
arr = [0]*m
def sol(c, d):
    if d == m:
        for i in arr:
            print(i, end=" ")
        print()
        return
    for i in range(c, n+1):
        arr[d] = i
        sol(i, d+1)
sol(1, 0)