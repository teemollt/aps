data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7   #노드(정점)의 개수
#인접리스트
adj=[[] for _ in range(N+1)]

for i in range(0,len(data),2):
    #무향 그래프 이므로 양쪽에 모두 추가
    s = data[i]
    e = data[i+1]
    adj[s].append(e)
    adj[e].append(s)


#bfs 는 먼저 발견한 경로를 먼저 탐색하기 때문에 queue로써 작성하는 것이 적합하다.
#s : 시작 정점
def bfs(s):
    visited = [0]*(N+1)
    queue = list()
    queue.append(s)
    visited[s] = 1

    result = []
    #큐안에 있는 모든 정점을 다 검사할때 까지 계속 반복
    while queue:
        #큐에 가장 빨리 들어온 정점에 방문해서 해당 노드에서 갈 수 있는 길 있으면
        #모두 큐에 넣어주기 
        current = queue.pop(0)  #리스트에서 가장 빨리 들어온 요소는 0번 요소
        result.append(current)
        # visited[current] = 1
        #current에서 갈 수 있는 경로 모두 찾아주기
        for i in range(len(adj[current])):
            if visited[adj[current][i]] == 0:   #방문하지 않았으면,
                queue.append(adj[current][i])   #큐에 추가
                visited[adj[current][i]] = 1
    return result

result = bfs(1)
print(result)