# m, n, h 가로 세로 높이 가장 아래 상자부터 주어짐
import sys
from collections import deque
input = sys.stdin.readline
m, n , h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k, 0))
def sol(q):
    global arr
    dz, dy, dx = [0, 0, 0, 0,-1, 1], [-1, 0, 1, 0, 0, 0], [0, 1, 0, -1, 0, 0]
    dt = 0
    while q:
        cz, cy, cx, dt = q.popleft()
        for d in range(6):
            nz, ny, nx = cz+dz[d], cy+dy[d], cx+dx[d]
            if 0<=ny<n and 0<=nx<m and 0<=nz<h:
                if arr[nz][ny][nx] == -1:
                    continue
                elif not arr[nz][ny][nx]:
                    q.append((nz, ny, nx, dt+1))
                    arr[nz][ny][nx] = 1
    return dt
rst = sol(q)
def check(rst):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not arr[i][j][k]:
                    return -1
    return rst
print(check(rst))