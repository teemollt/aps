# import sys
# sys.stdin = open("sample_input (4871).txt")

def dfs(a):
    visited[a] = 1
    route.append(a)
    for i in range(1, v+1):
        if graph[a][i] == 1 and visited[i] == 0:
            dfs(i)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    graph = [[0] * (v+1) for _ in range(v+1)]
    # 이중배열 만들기
    for i in range(e):
        r = arr[i][0]
        c = arr[i][1]
        graph[r][c] = 1
    # print(s, g)
    visited = [0] * (v+1)
    route = []
    dfs(s)
    if s in route and g in route:
        rst = 1
    else:
        rst = 0
    print('#{} {}'.format(tc, rst))

