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

#재귀를 이용한 dfs
#v: 현재 방문중인 노드번호
#visited : 노드 방문여부 표시 배열
def dfs(v,visited):
    visited[v] = 1
    #v번 노드에서 갈 수 있는 모든 경로 탐색
    result = [v]
    for i in range(len(adj[v])):
        # adj[v][i] v와 연결되어있는 노드
        if visited[adj[v][i]] == 0:
            result += dfs(adj[v][i],visited)
    return result

result = dfs(1,[0]*(N+1))
print(result)