a = [1, 2, 1, 3, 1, 8, 2, 1, 2, 7, 3,1, 3, 4, 3, 5, 4,3,4,5,5,3,5,4,6,7,7,6,7,8,8,1,8,7]
v = 8
arr = [[0]*(v+1) for _ in range(v+1)]

def dfs(s):
    visited = [0] * (v + 1)
    stack = []
    visited[s] = 1
    stack.append(s)
    print(s, end=" ")
    while stack:
        top = stack[-1]
        for i in range(1, v+1):
            if arr[top][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                print(i, end=" ")
                break
        else:
            stack.pop()

# visited = [0] * (v + 1)
# def dfs2(s):
#     visited[s] = 1
#
#     for i in range(1, v+1):
#         if arr[s][i] == 1 and visited[i] == 0:
#             dfs2(i)






for i in range(0, len(a), 2):
    arr[a[i]][a[i + 1]] = 1

dfs(1)







