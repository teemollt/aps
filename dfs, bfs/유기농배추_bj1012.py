import sys
input = sys.stdin.readline
def sol(x, y):
    global arr, visited
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = []
    q.append((x, y))
    visited[y][x] = 1
    while q:
        

t = int(input())
for tc in range(t):
    # 배추밭 가로, 세로, 배추 심어져있는 위치 개수
    m, n, k = map(int, input().split())
    arr = [[0]*(m+1) for _ in range(n+1)]
    visited = [[0]*(m+1) for _ in range(n+1)]
    # 배추의 위치 k줄에 걸쳐 x, y
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

