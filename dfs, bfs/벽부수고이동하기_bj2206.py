import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*m for _ in range(n)] for _ in range(2)]
def bfs(x, y, visited):
    dy, dx, dt = [-1, 0, 1, 0], [0, 1, 0, -1], 1
    q = []
    ws = 1
    q.append((y, x, dt, ws))
    visited[0][y][x] = 1
    if x == m-1 and y == n-1:
        return dt
    while q:
        cy, cx, dt, ws = q.pop(0)
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0<=ny<n and 0<=nx<m:
                if ny == n-1 and nx == m-1:
                    return dt + 1
                if ws:
                    if arr[ny][nx] == 0 and visited[0][ny][nx] == 0:
                        q.append((ny, nx, dt+1, ws))
                        visited[0][ny][nx] = 1
                    elif ws and not visited[0][ny][nx] and arr[ny][nx]:
                        q.append((ny, nx, dt + 1, ws-1))
                        visited[1][ny][nx] = 1
                else:
                    if arr[ny][nx] == 0 and visited[1][ny][nx] == 0:
                        q.append((ny, nx, dt+1, ws))
                        visited[1][ny][nx] = 1

    return -1
print(bfs(0,0, visited))
