# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
#인접행렬(adjacency matrix)을 이용해서 그래프 표현이 가능
#정점의 개수  : 7
#간선의 개수 :  8
V = 7
E = 8
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
#인접행렬은 인덱스의 번호를 정점의 번호와 매칭시켜서 사용
# 정점이 1번부터 시작이라면, 정점의 개수보다 1더큰 크기의 인접행렬을 사용
adj = [[0] * (V+1) for _ in range(V+1)]
#2개의 정점정보가 한 쌍이니까 2개씩 읽어옴
for i in range(0,E*2,2):
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1
# 해야할일 이제 인접행렬 가지고 dfs 수행하기
#dfs 구현법 : 1. 반복문과 stack을 이용함, 2. 재귀를 이용함
def dfs(v): #v : 시작정점
    stack = list()
    #한 번 방문한 노드를 재 방문하지 않기 위해서 표시하는 배열
    #각 인덱스 노드 번호가 됨, 방문안했으면 0,방문했으면 1
    visited = [0] * (V+1)
    stack.append(v) # 시작정점을 stack에 넣어주기
    visited[v] = 1  #시작 정점을 방문했음을 표시
    print(v,end= " ") # 방문순서를 확인하기 위한, 출력
    # 스택이 비어있지 않을때 까지 아래를 반복
    #스택의 탑에 위치한 정점을 확인
        # 해당정점에서 갈 수 있는 경로가 있는가??
        # 갈 수있는 경로가 있으면, 새로운 경로를 stack에 push
        # 갈 수있는 경로가 없으면, pop
    # while len(stack) > 0:
    while stack: #스택의 요소가 있으면, 계속 반복
        # 스택의 탑에 위치한 정점을 확인
        top = stack[-1]
        # 해당정점에서 갈 수 있는 경로가 있는가?? : 인접행렬을 확인함
        # 갈 수있는 경로가 있으면, 새로운 경로를 stack에 push
        #인접행렬의 top 행을 순회
        for i in range(1,V+1):
            #인접행렬의 요소가 1이면 현재 위치에서 갈 수 있는 길이 있음
            #한 번도 방문하지 않았던 정점을 방문
           if adj[top][i] == 1 and visited[i] == 0:
               #갈 수 있는 정점
                stack.append(i)
                visited[i] = 1  #i번 노드에 방문했음을 표시
                print(i,end= " ")  # 방문순서를 확인하기 위한, 출력
                break  # 경로 찾았으면 즉시 해당 경로로 이동하기 위해서, break
        # 갈 수있는 경로가 없으면, pop
        else:  #for문의 break가 실행되지 않음 => 경로가 없음
            stack.pop()

#재귀를 이용한 dfs 구현 ,
# v : 현재 정점
#방문배열 선언
visited = [0]*(V+1)
def dfs2(v):
    #현재 정점을 방문했음을 표시
    visited[v] = 1
    # 현재 정점에서 갈 수 있는 경로를 확인 인접행렬과, 방문배열
    print(v,end=" ")
    for i in range(1,V+1):
        # 인접행렬 확인
        if adj[v][i] == 1 and visited[i] == 0:
            # 갈 수 있는 경로가 있으면, 재귀 실행
            dfs2(i)

#번외 : 반복과 stack을 이용하는데, 중간에 경로 찾으면 break 하는 부분을 빼봅시다.
def dfs3(v):
    stack = list()
    visited = [0]*(V+1) # 각정점의 방문여부 확인
    #시작정점 stack에 넣어주고 방문 표시
    stack.append(v)
    visited[v] = 1
    # print(v,end=" ")
    #stack의 top에 있는 정점에서 갈 수 있는 경로 찾기 : 반복
    #위 방법이랑 다른점은, 한 정점에 방문하면, 해당 정점에서
    # 방문할 수 있는 모든 정점을 stack에 넣어 줌
    # 해당정점은 재 방문할 필요가 없음
    while stack:    #stack이 비어있지 않으면 계속 반복
        top = stack.pop()
        print(top, end=" ")
        #top에 있는 정점에서 갈 수 있는 경로 인접행렬에서 확인하기
        for i in range(1,V+1):
            if adj[top][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = 1

# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
#dfs 수행
dfs(1)
print()
dfs2(1)
print()
dfs3(1)















