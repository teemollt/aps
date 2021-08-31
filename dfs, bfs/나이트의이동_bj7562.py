import sys
from collections import deque
input = sys.stdin.readline
def bfs(x, y, visited):
    q = deque()
    dy, dx, dt = [-2, -1, 1, 2, 2, 1, -1, -2], [1,2,2,1,-1,-2,-2,-1], 0
    if x == tx and y == ty:
        return dt
    q.append((y, x, dt))
    visited[y][x] = 1
    while q:
        cy, cx, dt = q.popleft()
        for d in range(8):
            ny, nx = cy+dy[d], cx+dx[d]
            if 0<=ny<l and 0<=nx<l:
                if ny == ty and nx == tx:
                    return dt+1
                if not visited[ny][nx]:
                    q.append((ny, nx, dt+1))
                    visited[ny][nx] = 1
t = int(input())
for tc in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    visited = [[0]*l for _ in range(l)]
    print(bfs(sx, sy, visited))
