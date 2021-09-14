# import sys
# sys.stdin = open("sample_input (최장).txt")

def sol(idx, d):
    global u, max_d
    u[idx] = 1
    if d > max_d:
        max_d = d
    for i in range(n+1):
        if not u[i] and arr[idx][i]:
            sol(i, d+1)
    u[idx] = 0


t = int(input())
for tc in range(1, t+1):
    # n개 정점, m개 간선
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    u = [0] * (n+1)
    max_d = 0
    for i in range(1, n+1):
        sol(i, 1)
        # u = [0] * (n + 1)
    print('#{} {}'.format(tc, max_d))