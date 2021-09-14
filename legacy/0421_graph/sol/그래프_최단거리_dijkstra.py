# Dijkstra 다익스트라: 최단거리
# 특정 정점에서 다른 나머지 정점까지 가는 최단거리를 구하는 알고리즘
# 1. 각 정점까지 걸리는 시간을 최대로 설정하고,
# 2. 새로운 경로가 생길 때 마다, 해당경로를 이용하는 비용계산
#    2-1 계산한 비용이 기존 경로보다 더 작다면, 해당 경로비용으로 갱신
# 3. 모든 노드가 선택될때 까지 반복
# 6 10
# 1 2 3
# 1 3 4
# 2 4 5
# 3 2 1
# 3 4 4
# 3 5 5
# 4 5 3
# 4 6 4
# 5 1 3
# 5 6 5
def dijkstra(start,adj,weight):
    #노드로 가는 비용이 확정된 노드들을 저장하는 집합 U
    U = {start}
    # 모든 노드들이 선택될때 까지 아래사항(1,2)을 반복
    # 1.현재 선택된 노드들을 통해서, 갈수있는 경로 중 최소 비용을 가지는 경로를 선택
    # 2. 새로운 노드가 선택되면, 경로비용을 업데이트(만약에 경로비용이 더 작은 비용이 생긴다면)
    while len(U) < V:
        min_w = 0xfffffff
        min_idx = -1
        #weight 비용확인하면서, 아직 추가 안된 노드중, 최소 비용 찾기
        for i in range(1, V+1):
            #아직 해당 노드가 선택되지 않았고,
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i
    
        #최소 비용을 가지는 노드를 찾았음
        U.add(min_idx)
        #지금 선택된 노드를 통해서 다른노드들로 갈 수 있는 경로의 비용을 업데이트
        for i in range(1,V+1):
            if i not in U:
                # 아직 선택되지 않은 노드들의 경로 비용을 다시 계산
                # min_idx에서 i번 노드로 가는 비용 + 시작에서 min_idx로 가는 비용
                tmp = weight[min_idx] + adj[min_idx][i]
                if weight[i] > tmp: #min_idx를 거쳐서 i번으로 가는 경로 비용이 더 적음
                    weight[i] = tmp

    return weight



V, E = map(int,input().split())
INF = 0xfffffff
adj = [[INF]*(V+1) for _ in range(V+1)]
for i in range(E):
    s,e,w = map(int,input().split())
    adj[s][e] = w

#시작정점: 1
start = 1
#시작정점에서 다른 정점들 까지 가는데 드는 비용(가중치) 배열
weight = adj[start][:]  #인접행렬의 start 행이... 초기 weight가 됩니다.
result = dijkstra(start,adj,weight)
print(result)

