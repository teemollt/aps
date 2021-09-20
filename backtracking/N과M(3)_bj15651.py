n, m = map(int, input().split())
arr = [0]*m
def sol(d):
    if d == m:
        for i in arr:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        arr[d] = i
        sol(d+1)
sol(0)