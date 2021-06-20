# V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.

def bfs(arr, start, d, visited):
    # queue
    q = []
    q.append((start, d))
    while q:
        cv, cd = q.pop(0)
        visited[cv] = 1
        for i in range(v+1):
            if arr[cv][i] and not visited[i]:
                if i == g:
                    return cd+1
                q.append((i, cd+1))
    return 0

t = int(input())
for tc in range(1, t+1):
    # v개의 노드, e개의 간선
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    visited = [0] * (v+1)
    # e개의 줄에 걸쳐 간선 양쪽의 노드 번호
    for n in range(e):
        l, r = map(int, input().split())
        arr[l][r] = 1
        arr[r][l] = 1
    # 출발노드 s, 도착노드 g
    s, g = map(int, input().split())
    # 함수 실행
    print(f'#{tc} {bfs(arr, s, 0, visited)}')
