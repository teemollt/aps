# swea [파이썬 S/W 문제해결 기본] 그래프 경로
# Learn Course Programming Intermediate 파이썬 SW문제해결 기본 - Stack1
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
# 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

# 반복, 행렬
def dfs(arr, d, visited):
    global rst
    # 스택 리스트
    stack = []
    # 출발노드 추가
    stack.append(d)
    visited[d] = 1
    # 스택이 완전히 빌때까지 반복
    while stack:
        # 스택 맨위 뽑기 == 현재 노드
        node = stack.pop()
        if node == target:
            rst = 1
            return
        # 현재 노드에서 갈수 있는 노드 탐색
        for i in range(v+1):
            if arr[node][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1

# 재귀, 행렬
def dfs_rc(arr, d, visited):
    global rst
    visited[d] = 1
    # print(d, end="-")
    for i in range(v+1):
        if arr[d][i] and not visited[i]:
            if i == target:
                rst = 1
                return
            dfs_rc(arr, i, visited)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    # 인접행렬
    arr = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        s, g = map(int, input().split())
        arr[s][g] = 1
    depart, target = map(int, input().split())
    visited = [0] * (v+1)
    rst = 0
    # dfs_rc(arr, depart, visited)
    # print(f'#{tc} {rst}')
    dfs(arr, depart, visited)
    print('#{} {}'.format(tc, rst))

