import sys, heapq
input = sys.stdin.readline

def sol():
    V, E = map(int, input().split())
    K = int(input())
    inf = int(1e9)
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    # 최단거리 테이블 / 시작점에서 인덱스까지 가는 최단거리(아래에서 계속 갱신해줄거임)
    dis = [inf] * (V+1)
    for _ in range(E):
        u, v, e = map(int, input().split())
        # 출발점 u 도착점 v 비용 e
        arr[u].append((v, e))
    def djk(start):
        # 큐에는 (거리, 도착노드) 담아줌
        q = []
        # 시작노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입 시작점-> 시작점이니까
        heapq.heappush(q, (0, K))
        dis[start] = 0
        # 큐가 빌때까지
        while q:
            # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 팝하면 가장 작은 값이 나옴
            # 따라서 now는 현위치, d는 시작점에서 그 위치까지 거리
            d, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된적 있는 노드라면 무시 / (현재 꺼낸값이 테이블에 있는 값보다 크면 이미 처리된거)
            if dis[now] < d:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            # arr[now]에는 (현위치에서 갈수있는 노드번호, 그 거리)튜플이 들어있음
            for i in arr[now]:
                # d => 시작점에서 현위치까지의 거리 / i[1] => 현위치에서 인접한 노드까지의 거리 / +=> 시작점에서 현위치-인접노드까지의 거리
                cost = d + i[1]
                # 시작점에서 인접노드까지의 총거리가 dis에 담겨있는 인접노드까지의 최단거리와 비교해서 더 작으면 갱신
                if cost < dis[i[0]]:
                    dis[i[0]] = cost
                    # 큐에다가도 해당내용을 푸쉬
                    heapq.heappush(q, (cost, i[0]))
            print(q)
    djk(K)
    for i in range(1, V+1):
        if dis[i] == inf:
            print("INF")
        else:
            print(dis[i])
sol()