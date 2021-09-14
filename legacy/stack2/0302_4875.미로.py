import sys
sys.stdin = open("sample_input (4875).txt")
# dfs
def dfs(y, x):
    global visited
    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 방문처리
    visited[y][x] = 1
    ahahahh = maze[y][x]
    # 도착시 결과값 리턴
    if maze[y][x] == 3:
        return 1
    # 사방향 탐색
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (maze[ny][nx] == 0 and visited[ny][nx] == 0) or (maze[ny][nx] == 3 and visited[ny][nx] == 0):
            if dfs(ny, nx):
                return 1
    return 0

t = int(input())
for tc in range(1, t+1):
    # n * n 미로
    n = int(input())
    # 벽으로 둘러싼 미로 초기화
    maze = [[1]*(n+2) for _ in range(n+2)]
    # 0 통로 / 1 벽 / 2 출발 / 3 도착 미로 입력
    for i in range(1, n+1):
        row = input()
        for j in range(n):
            maze[i][j+1] = int(row[j])
    # print(maze)
    rst = 0
    visited = [[0] * (n + 2) for _ in range(n + 2)]
    # 출발점 찾기
    for i in range(1, n+1):
        for j in range(1, n+1):
            if maze[i][j] == 2:
                # 함수 실행
                rst = dfs(i, j)
            if rst:
                break
    print('#{} {}'.format(tc, rst))