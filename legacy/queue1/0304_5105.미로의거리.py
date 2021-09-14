import sys
sys.stdin = open("sample_input (5105).txt")
# 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0
def solve(y, x, distance):
    global visited
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited[y][x] = 1
    # 큐에 넣고 제일 앞에 있는거 뽑아서 검사
    q = []
    p = (y, x, distance)
    q.append(p)
    # 큐가 빌때까지 반복
    while q:
        # 현위치
        cy, cx, distance = q.pop(0)
        # 4방향 탐색
        for d in range(4):
            # 검색위치의 값이 0이고 방문한적 없으면 큐에 추가
            if not arr[cy+dy[d]][cx+dx[d]] and not visited[cy+dy[d]][cx+dx[d]]:
                q.append((cy+dy[d], cx+dx[d], distance+1))
                visited[cy+dy[d]][cx+dx[d]] = 1
            # 3이면 도착이니까 멈추고 거리반환
            elif arr[cy+dy[d]][cx+dx[d]] == 3:
                return distance
        # 거리 1추가
        distance += 1

    # while문 다돌았는데 리턴 안됐으면 도착 못한거니까 0 리턴
    return 0




t = int(input())
for tc in range(1, t+1):
    # 미로크기 n * n
    n = int(input())
    # 미로 입력 0은 통로, 1은 벽, 2는 출발, 3은 도착 / 사방을 벽으로 둘러싸자...
    arr = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        num = input()
        for j in range(n):
            arr[i+1][j+1] = int(num[j])
    # print(arr)
    visited = [[0] * (n+1) for _ in range(n+1)]
    rst = 0
    # 출발점 찾기 2
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == 2:
                rst = solve(i, j, 0)
                break
    print('#{} {}'.format(tc, rst))