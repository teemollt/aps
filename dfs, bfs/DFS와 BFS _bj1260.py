from sys import stdin
input = stdin.readline
n, m, v = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1
visited = [0] * (n+1)
def dfs(arr, v, visited):
    print(v, end=" ")
    visited[v] = 1
    for i in range(1, n+1):
        if arr[v][i] and not visited[i]:
            dfs(arr, i, visited)

def bfs(arr, v, visited):
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

dfs(arr, v, visited)
visited = [0] * (n+1)
print()
bfs(arr, v, visited)
