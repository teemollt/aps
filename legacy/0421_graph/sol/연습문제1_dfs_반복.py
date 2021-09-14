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

# for row in adj:
#     print(row)

# 재귀, 반복+stack
#1. 반복 + dfs
#s : 탐색 시작 노드
def dfs(s):
    visited = [0]*(N+1)
    stack= list()

    #stack에는 지나온 정점을 넣어주는데,
    #stack의 top에 있는 요소가 현재 방문 위치
    stack.append(s)
    #stack에 있는 모든 정점을 방문
    #만약에 해당 정점에서 갈 수 있는 경로가 없으면
    #해당 정점을 stack에서 pop
    #stack이 비어있지 않으면
    #stack의 top에서 갈 수 있는 경로를 탐색하는 과정을 반복
    result_lst = [s]    # 경로 출력해야 하니까
    while len(stack) > 0:
        #stack의 top 확인
        current = stack[-1]
        visited[current] = 1
        #현재 정점에서 갈 수 있는 경로가 잇는지 확인하고
        #갈 수 있는 경로가 있으면, 즉시 다음 경로로 진행
        #(stack에 다음 노드 push하고, 경로 탐색 종료)
        #현재 위치에서 갈 수 있는 경로 탐색
        for i in range(len(adj[current])):
            if visited[adj[current][i]] == 0:
                stack.append(adj[current][i])
                result_lst.append(adj[current][i])

                break
        #for-else : for문이 break 없이 모두 수행되었을때 실행
        else:   #갈 수 있는 경로가 없음
            stack.pop()
    return result_lst


result = dfs(1)
print(result)