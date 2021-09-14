import sys
sys.stdin = open("sample_input (node).txt")

def bfs(s, g, d):
    global visited
    q = []
    visited[s] = 1
    # q에 방문노드, 거리 저장
    q.append((s, d))
    # q가 빌때까지 탐색
    while q:
        # 큐에서 하나 빼서 기준으로
        no = q.pop(0)
        if no[0] == g:
            return no[1]
        # 연결된곳 탐색
        for i in range(1, v+1):
            # 연결됐고 방문안했으면 큐에 넣기
            if arr[no[0]][i] and not visited[i]:
                q.append((i, no[1]+1))
                visited[i] = 1
    return 0
t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    # 인접행렬
    arr = [[0] * (v + 1) for _ in range(v+1)]
    # e개 줄에 걸쳐 양쪽 노드번호
    for i in range(e):
        l, r = map(int, input().split())
        arr[l][r] = 1
        arr[r][l] = 1
    # 출발 s 도착 g
    s, g = map(int, input().split())
    # print(arr)
    visited = [0] * (v + 1)
    rst = bfs(s, g, 0)
    print('#{} {}'.format(tc, rst))
