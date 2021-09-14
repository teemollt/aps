def dfs(S,G):
    stack = list()
    visited = [0] * (V+1)
    #시작 정점 방문처리
    stack.append(S)
    visited[S] = 1

    #stack이 비어있지 않으면, 탐색 반복
    while stack:
        top = stack.pop()
        if top == G:
            return 1
        #현재 노드에서 갈 수 있는 경로 모두 탐색
        for i in range(1,V+1):
            #top에서 i번 정점으로 갈 수 있는 경로가 있고,
            #i번 정점을 아직 방문하지 않았다면, 방문
            if adj[top][i] == 1 and visited[i] == 0:
                #stack에 push하고, 방문배열 표시
                stack.append(i)
                visited[i] = 1
    #dfs 탐색이 끝났는데, G에 도착 못했다면, 경로가 없는것
    return 0

#재귀를 이용한 dfs
#N: 현재 탐색중인 노드의 번호
#경로가 있으면 1을 반환, 없으면 0을 반환하는 함수
def dfs2(N):
    # global result
    visited[N] = 1
    #경로를 찾았음
    if N == G:
        # result = 1
        return 1
    #N에서 갈 수 있는 경로를 탐색
    for i in range(1,V+1):
        if adj[N][i] and not visited[i]:
            # result = dfs2(i)
            # if result  == 1:
            #     return 1
            if dfs2(i):
                return 1
            # dfs2(i)
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    #노드의 번호가 1번부터 시작하니까... 인덱스를 노드 번호로 
    #사용하기 위해서 V+1 인 크기의 인접행렬 생성
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V + 1)
    for i in range(E):
        s,e = map(int,input().split())
        #그래프의 모양은 인접행렬로 표현
        adj[s][e] = 1
    #시작, 목적지
    S, G = map(int,input().split())
    # print("#{} {}".format(tc, dfs(S,G)))
    # result = 0
    print("#{} {}".format(tc,dfs2(S)))