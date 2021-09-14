a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
v = 7
arr = [[0]*(v+1) for _ in range(v+1)]
for i in range(0, len(a), 2):
    arr[a[i]][a[i+1]] = 1

# s : 시작 정점
def bfs(s):
    # bfs는 먼저 방문한 정점이 먼저 버려진다. >> queue를 사용
    queue = []
    # 한번 방문한 정점을 확인하기 위한 visited
    visited = [0] * (v+1)
    queue.append(s)
    visited[s] = 1
    # 1. queue에서 가장 앞에 있는 정점을 방문
    # 2. 해당 정점에서 방문할 수 있는 모든 경로를 저장: queue에 순서대로 넣어줌
    # 3. 1~2번을 queue가 빌때 까지 반복한다.
    while queue:
        front = queue.pop(0)   # queue에서 가장 앞에 있는 정점을 가져옴
        # pop하는 순간 방문 / 방문순서 출력
        print(front, end=" ")
        # front에서 갈 수 있는 경로를 탐색
        for i in range(1, v+1):
            # 인접행렬이 1이면 경로가 있는것, 방문하지 않은 정점을 방문해야함
            if arr[front][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1
    print()

    bfs(1)