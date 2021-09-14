#v : 현재 노드 번호
#d : 경로 길이
def dfs(v,d):
    global max_length
    visited[v] = 1
    #현재 길이가 최장인지 확인
    if max_length < d:
        max_length = d
    #갈 수 있는 모든 경로 탐색
    for i in range(1,N+1):
        if adj[v][i] and not visited[i]:
            dfs(i,d+1)  # 다음 경로 길이는 현재 경로길이 +1
    visited[v] = 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        adj[a][b] = 1
        adj[b][a] = 1

    visited = [0]*(N+1)
    #순회 시작 위치에 따라서 경로길이가 달라질 수 있음
    #탐색은 모든 정점에서 시작해보기
    max_length = 0
    for i in range(1,N+1):
        #순회 시작
        dfs(i,1)
    print("#{} {}".format(tc,max_length))









