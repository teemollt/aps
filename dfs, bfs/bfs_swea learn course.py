# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
# NxN 크기의 미로에서 출발지 목적지가 주어진다.
# 이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
# 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

def bfs(x, y, d, visited):
    # 상하좌우 이동을 위한..
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # queue
    q = []
    # 현위치 큐에 넣기
    q.append((x, y, d))
    # 큐가 빌때까지 반복
    while q:
        cx, cy, cd = q.pop(0)
        visited[cy][cx] = 1
        for dir in range(4):
            # 인덱스 에러 방지 범위 설정
            if 0 <= cy+dy[dir] < n and 0 <= cx+dx[dir] < n:
                ny = cy+dy[dir]
                nx = cx+dx[dir]
                if arr[ny][nx] == 3:
                    return cd
                if not arr[ny][nx] and not visited[ny][nx]:
                    q.append((nx, ny, cd+1))
    return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                print(f'#{tc} {bfs(j, i, 0, visited)}')
