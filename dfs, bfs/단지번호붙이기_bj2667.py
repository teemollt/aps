from sys import stdin
input = stdin.readline
n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
rst = []
def sol(x, y):
    global arr, visited
    arr[y][x] = 0
    q = []
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited[y][x] = 1
    q.append((y, x))
    arr[y][x] = 0
    cnt = 1
    while q:
        cy, cx = q.pop(0)
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1
                arr[ny][nx] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            rst.append(sol(j, i))
rst.sort()
print(len(rst))
for r in rst:
    print(r)
