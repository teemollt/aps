import sys
sys.stdin = open("input (hw).txt")
# 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점
def sol(y, x, d):
    global visited
    # 사방 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = []
    # 출발점 방문표시, 큐에 추가
    visited[y][x] = 1
    q.append((y, x, d))
    # 사방탐색 고고
    # 큐가 빌때까지 탐색
    while q:
        # 큐에서 꺼내서 현위치/거리
        cy, cx, cd = q.pop(0)
        # 현위치기준 사방 탐색
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if not arr[ny][nx] and not visited[ny][nx]:
                # 조건에 맞으면 큐에 추가 / 방문처리
                q.append((ny, nx, cd + 1))
                visited[ny][nx] = 1
            elif arr[ny][nx] == 3:
                return 1
    return 0

t = 10
for _ in range(1, t+1):
    tc = int(input())
    # 미로 입력
    arr = [[1]*16 for _ in range(16)]
    for i in range(16):
        num = input()
        for j in range(16):
            arr[i][j] = int(num[j])
    # 방문표시할 행렬
    visited = [[0]*16 for _ in range(16)]
    # 출발지점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                rst = sol(i, j, 0)
    print('#{} {}'.format(tc, rst))

