import sys
sys.stdin = open("sample_input (4881).txt")

# 사용한 줄 표시하기 위한 리스트


def dfs(y, x):
    # 방문처리
    visited[y][x] = 1
    idx_x[x] = 1
    idx_y[y] = 1
    stack.append(arr[y][x])
    for i in range(n):
        if 0 <= i < n:
            




t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    idx_x = [0] * n
    idx_y = [0] * n
    stack = []
    # print(arr)
    # 한줄에 하나씩이니까 첫번째줄 요소 하나 시작점 잡고 dfs
    dfs(0, 0)
    /

