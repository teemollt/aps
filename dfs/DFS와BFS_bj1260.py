# baekjun 1260 BFS와  DFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력

def dfs(arr, visited, v):
    # 현재노드 출력
    print(v, end=" ")
    visited[v] = 1
    for i in range(1, n+1):
        if arr[v][i] and not visited[i]:
            dfs(arr, visited, i)


def bfs(arr, visited, v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        c = q.pop(0)
        print(c, end=" ")
        for i in range(1, n+1):
            if arr[c][i] and not visited[i]:
                q.append(i)
                visited[i] = 1

# 입력
n, m, v = map(int, input().split())

arr = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

# 출력
dfs(arr, visited, v)
print()
visited = [0] * (n+1)
bfs(arr, visited, v)