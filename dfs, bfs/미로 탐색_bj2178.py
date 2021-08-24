import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
def sol(y, x, dt):
    global visited
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = []
    q.append((y, x, dt))
    while q:
        cy, cx, dt = q.pop(0)
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if nx == m-1 and ny == n-1:
                return dt+1
            elif 0<=ny<n and 0<=nx<m and not visited[ny][nx] and arr[ny][nx]:
                q.append((ny, nx, dt+1))
                visited[ny][nx] = 1

print(sol(0,0,1))
