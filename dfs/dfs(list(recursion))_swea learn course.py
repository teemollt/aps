# swea [파이썬 S/W 문제해결 기본] 그래프 경로
# Learn Course Programming Intermediate 파이썬 SW문제해결 기본 - Stack1
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
# 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

# 재귀 인접리스트
def dfs(arr, v, visited):
    global rst
    # 시작점 v 방문처리
    visited[v] = 1
    # print(v, end="-")
    # 리스트 전체 돌면서
    for i in range(0, e*2, 2):
        # i가 v랑 같은지 확인, 같으면 연결된 노드가 이미 방문한 곳인지 확인
        if arr[i] == v and not visited[arr[i+1]]:
            # target으로 이동 가능하면 rst에 1을 저장
            if arr[i+1] == target:
                rst = 1
            # 조건 통과하면 연결된 노드를 출발점으로 함수 실행
            dfs(arr, arr[i+1], visited)

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    # 인접리스트
    arr = []
    for i in range(e):
        s, g = map(int, input().split())
        arr.append(s)
        arr.append(g)
    depart, target = map(int, input().split())
    visited = [0] * (v+1)
    rst = 0
    dfs(arr, depart, visited)
    print(f'#{tc} {rst}')