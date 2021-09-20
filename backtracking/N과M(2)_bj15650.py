n, m = map(int, input().split())
arr = [0]*m
used = [0]*(n+1)
def sol(k, d):
    if d == m:
        for i in arr:
            print(i, end=" ")
        print()
        return
    for i in range(k+1, n+1):
        if not used[i]:
            arr[d] = i
            sol(i, d+1)
            used[i] = 0
sol(0,0)