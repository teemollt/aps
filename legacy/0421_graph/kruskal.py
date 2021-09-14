# kruskal
# 1. 가중치의 크기 순서대로 정렬
# 2. 가중치가 작은 간선들을 하나씩 선택(간선에 포함되는 노드들이 MST에
# 3. 만약 간선들 선택하다가, 사이클이 생기면 선택하지 않는다.
# 3. n-1개 간선이 선택될때까지 (모든 노드들이 선택될때 까지) 위를 반복
import heapq
def union():
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    else:
        parent[b] = a

def find_set():
    if x == parent[x]:
        return
    return find_set(parent[x])

def kruskal():
    # 최소 가중치 비용을 저장할 변수
    result = 0
    # 1. 정렬
    data.sort(key=lambda x: x[2])
    # 2. 선택, 만약 사이클이 생기면 선택 안함.
    # 2-1 : 사이클이 생기는지 판단하기 : 서로소 집합 이용하기
    mst = []
    # data를 하나씩 읽으면서, 사이클이 생기는지 확인
    for i in range(e):
        # 서로소 집합의 대표가 같으면, 사이클이 생김 -> 아무작업 안함
        if find_set(data[i][0]) == find_set(data[i][1]):
            continue
        # 아니라면, 집합 합쳐주고, 간선 선택
        union(data[i][0], data[i][1])
        mst.append((data[i][0], data[i][1], data[i][2]))
        result += data[i][2]



v, e = 7, 11

for tc in range(e):
    a,b,w = map(int, input().split())

data =list()
parent = list(range(v))