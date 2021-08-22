from sys import stdin
input = stdin.readline
n = int(input())
e = int(input())
arr = [[] for _ in range(n+1)]
for i in range(e):
    l, r = map(int, input().split())
    arr[l].append(r)
    arr[r].append(l)

visited = [0] * (n+1)
cnt = 0
def sol(arr, v, visited, cnt):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        c = q.pop(0)
        if arr[c]:
            for i in arr[c]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1

    return cnt
print(sol(arr, 1, visited, cnt))