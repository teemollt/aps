import sys
sys.stdin = open("s_input(chang).txt")

def find_set(x):
    # if x == p[x]:
    #     return x
    # return find_set(p[x])
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    global p
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    else:
        if a < b:
            p[b] = a
        else:
            p[a] = b


t = int(input())
for tc in range(1, t+1):
    #마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는 두 정수 N, M
    n, m = map(int, input().split())
    arr = [[0]*(n+1) for _ in range(n+1)]
    p = [0] * (n+1)
    check = [0] * (n+1)
    for i in range(n+1):
        p[i] = i

    # 인접행렬
    for _ in range(m):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j]:
                union(i, j)

    for i in range(1, n+1):
        if i == p[i]:
            check[i] = 1
    cnt = 0
    for i in check:
        if i:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
