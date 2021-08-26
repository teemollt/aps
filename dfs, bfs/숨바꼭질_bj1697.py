from collections import deque
n, k = map(int, input().split())
def sol(n, k):
    if n == k:
        return 0
    q = deque()
    q.append((n, 0))
    arr = [0]*100001
    arr[k] = 2
    ct = 0
    while q:
        cx, ct = q.popleft()
        dx = [1, -1, cx]
        for d in range(3):
            nx = cx + dx[d]
            if 0<=nx<=100000:
                if arr[nx] == 2:
                    return ct+1
                elif not arr[nx]:
                    q.append((nx, ct+1))
                    arr[nx] = 1

print(sol(n, k))