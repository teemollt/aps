c = []
def dfs(x, v, computers, n):
    global c
    c.append(x)
    v[x] = 1
    for i in range(n):
        if computers[x][i] and not v[i]:
            dfs(i, v, computers, n)
def solution(n, computers):
    answer = 0
    v = [0] * n
    for i in range(n):
        if i not in c:
            answer += 1
        dfs(i, v, computers, n)
    return answer