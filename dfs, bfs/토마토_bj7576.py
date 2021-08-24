import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j, 0))
def bfs(dt, q):
    global arr
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        cy, cx, dt = q.popleft()
        for d in range(4):
            ny, nx = cy+dy[d], cx+dx[d]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == -1:
                    continue
                elif not arr[ny][nx]:
                    q.append((ny, nx, dt+1))
                    arr[ny][nx] = 1
    return dt
def sol(arr):
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                return False
    return True

rst = bfs(0, q)
if sol(arr):
    print(rst)
else:
    print(-1)