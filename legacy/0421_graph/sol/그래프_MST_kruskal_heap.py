import heapq
def union(x,y):
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    else:
        parent[b] = a

def find_set(x):
    if x == parent[x]:
        return x
    return find_set(parent[x])

    # print(arr)
def kuruskal(data):
    #최소 가중치 비용을 저장할 변수
    result = 0
    #2. 선택,만약에 사이클이 생기면 선택안함
    # 2-1: 사이클이 생기는지 판단하기 : 서로소집합 이용하기
    mst = list()
    while data:
        w,e = heapq.heappop(data)
        if find_set(e[0]) == find_set(e[1]):
            continue
        mst.append((w,e))
        union(e[0],e[1])
        result += w
    print(mst)
    return result



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
#Kruskal
#1. 가중치의 크기 순서대로 정렬
#2. 가중치가 작은 간선들을 하나씩 선택(간선에 포함되는 노드들이 MST에 포함)
#3. 만약에 간선들을 선택하다가, 사이클이 생기면 선택하지 않는다.
#4. 모든 노드들이 선택될 때 까지 반복
V, E = map(int,input().split())
data = list()
parent = list(range(V))
#data를 heap형태로 저장하고 사용해보기
for e in range(E):
    a,b,w = map(int,input().split())
    # data.append((a,b,w))
    #heapq : 우선순위 큐, 기준설정해주면, 우선되는 요소가 먼저 pop
    #heappush(대상리스트,요소) : 요소의 첫번째 값이 기준이 됨
    heapq.heappush(data,(w,(a,b)))
result = kuruskal(data)
print(result)





