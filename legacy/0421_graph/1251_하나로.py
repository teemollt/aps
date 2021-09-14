import sys
sys.stdin = open("input (hana).txt")

def find_set(x, p):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    a = find_set(x, p)
    b = find_set(y, p)
    if a == b:
        return
    else:
        if a < b:
            p[b] = a
        else:
            p[a] = b

t = int(input())
for tc in range(1, t+1):
    # 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L2)만큼 지불
    # 총 환경 부담금을 최소로 지불하며, N개의 모든 섬을 연결
    # 섬의 개수 n
    n = int(input())
    location = []
    p = [0] * n
    for i in range(n):
        p[i] = i
    edges = []
    # 각 섬들의 정수인 X좌표 Y좌표
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for i in range(n):
        location.append((x[i], y[i]))
    # 해저터널 건설의 환경 부담 세율 실수 E
    e = float(input())
    # e * l * l = cost 각 섬을 연결하는 비용 계산 인접행렬 만들기
    arr = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            a = location[i]
            b = location[j]
            dx = abs(a[0]-b[0])
            dy = abs(a[1]-b[1])
            d = (dx**2) + (dy**2)
            arr[i][j] = d*e
            # arr[j][i] = d*e
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((arr[i][j], i, j))
    edges.sort()
    # print(edges[:3])
    rst = 0
    for i in edges:
        w, a, b = i
        if find_set(a, p) != find_set(b, p):
            union(a, b)
            rst += w
    print('#{} {}'.format(tc, round(rst)))
