
# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 6 25
# 2 4 46
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51

V,E = map(int,input().split())
#adj 각 노드간 가중치를 저장하는 인접행렬
INF = 0xfffffff
adj = [[INF]*V for _ in range(V)]
for i in range(E):
    s,e,w = map(int,input().split())
    adj[s][e] = w
    adj[e][s] = w

#prim 알고리즘을 통한 mst 가중치 얻어오기
#start: 시작 정점
def prim(start):
    # 1. 임의의 노드 설정
    # 2. 갈 수 있는 노드들까지 가는 비용이 제일 작은 노드를 선택한다.
    # 3. 단, 이미 선택된 노드라면 선택하지 않음.
    # 선택을 반복한다.
    # #가중치를 저장하는 배열, 초기값은 최대값
    INF = 0xfffffff #엄청 큰값으로 초기화,
    weight = [INF]*V
    weight[start] = 0
    #어떤 노드를 선택했는지 표시하는 배열
    mst = [0] * V   #0이면 아직 선택되지 않은 노드, 1이면 선택된 노드

    # 최소신장트리의 가중치를 저장하는 변수
    result = 0
    #어떤 노드가 어디에 연결되었는지 저장하는 배열
    st = [-1] * V
    #모든 노드들이 선택될 때 까지 가중치가 제일 작은 노드를 선택
    for _ in range(V):
        print(weight)
        #현재까지 선택된 노드들에서 갈 수 있는 모든 경로를 탐색하는데
        #그 중에서 가중치가 제일 작은 경로를 선택
        min_w = 0xffffff    #최소값을 선택하기 위한 변수
        min_v = 0
        for i in range(V):
            #살펴봐야 하는 상태
            #아직 선택안된 노드,
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i
        #현재 갈 수 있는 최소 가중치의 노드가 선택
        mst[min_v] = 1
        result += min_w     #노드가 선택되었으니 가중치 더하기

        #새로 선택한 정점으로부터 갈 수 있는 경로를 살펴보고
        #해당 노드를 선택하기 위한 가중치가 작아지면, 수정
        #weight[] 수정, min_v가 새롭게 추가된 노드
        #min_v에서 i번째로 가는 가중치가 , 기존 가중치 보다 작으면 업데이트
        for i in range(V):
            if adj[min_v][i] < weight[i] and mst[i]==0:
                weight[i] = adj[min_v][i]
                st[i] = min_v   #어느 노드에서 온 간선인지 저장
    return result

result=prim(0)
print(result)