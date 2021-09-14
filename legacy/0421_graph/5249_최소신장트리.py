import sys
sys.stdin = open("sample_input (mst).txt")

#
def find_set(x):
    # 자기 자신이 부모가 아니다 => 루트를 찾아올라가자
    if x == parent[x]:
        return x
    return find_set(parent[x])

def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a == b:
        # 이미 같은 집합이니까 그냥 리턴
        return
    # 아니면
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

t = int(input())
for tc in range(1, t+1):
    # 마지막 노드번호 V와 간선의 개수 E
    v, e = map(int, input().split())
    parent = [0] * (v+1)
    # 자기자신으로 초기화
    for i in range(v+1):
        parent[i] = i
    # print(parent)
    edges = []
    rst = 0
    for _ in range(e):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))
    # 비용순 정렬
    edges.sort()
    # print(edges)
    # print(edges)
    for i in edges:
        w, a, b = i
        # 싸이클 안되는 경우에만 포함
        if find_set(a) != find_set(b):
            union(a, b)
            rst += w
    print('#{} {}'.format(tc, rst))
