import sys
input = sys.stdin.readline
def sol(x, y):
    global arr, visited, rst
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = []
    q.append((x, y))
    visited[y][x] = 1
    while q:
        cx, cy = q.pop(0)
        for d in range(4):
            ny, nx = cy+dy[d], cx+dx[d]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = 1
    rst += 1
    return

t = int(input())
for tc in range(t):
    # 배추밭 가로, 세로, 배추 심어져있는 위치 개수
    m, n, k = map(int, input().split())
    arr = [[0]*(m) for _ in range(n)]
    visited = [[0]*(m) for _ in range(n)]
    rst = 0
    # 배추의 위치 k줄에 걸쳐 x, y
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                sol(j, i)
    print(rst)
