import sys, heapq
input = sys.stdin.readline
def sol():
    n, e = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(e):
        # a출발점 b도착점 c거리
        a, b, c = map(int, input().split())
        arr[a].append((b, c))
        # 양방향
        arr[b].append((a, c))
    req1, req2 = map(int, input().split())
    inf = int(1e9)
    def djk(start, end):
        d = [inf] * (n + 1)
        q = []
        heapq.heappush(q, (0, start))
        d[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if d[now] < dist:
                continue
            for i in arr[now]:
                # 현위치까지의 거리
                cost = dist + i[1]
                if cost < d[i[0]]:
                    d[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return d[end]
    rst = min((djk(1, req1) + djk(req1, req2) + djk(req2, n)), (djk(1, req2)+djk(req2, req1)+djk(req1, n)))
    # 실제로 1개의 경로라도 inf가 나오는 경우라면 연결이 안되는 것이기때문에 -1이 출력되어야함 즉 연결이 안된 경우엔
    # rst값이 inf보다 크기때문에 아래 같은 조건을 걸어줘야함
    if rst < inf:
        print(rst)
    else:
        print(-1)
sol()