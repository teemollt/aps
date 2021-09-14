V
visited = [0]*(V+1)
def dfs(v):
    visited[v] = 1
    print(v)
    for i in range(1, V+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)