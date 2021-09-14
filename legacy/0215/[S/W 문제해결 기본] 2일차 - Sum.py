import sys
sys.stdin = open("input (2).txt")


t = 10
for tc in range(1, t+1):
    n = 100
    arr = [[0]*n for _ in range(n)]
    max_v = 0
    total = 0
    tn = int(input())
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            total += arr[i][j]
            if max_v < total:
                max_v = total
        total = 0

        for j in range(n):
            total += arr[j][i]
            if max_v < total:
                max_v = total
        total = 0

    for i in range(n):
        total += arr[i][i]
        if max_v < total:
            max_v = total
        total = 0
        total += arr[n-1-i][i]
        if max_v < total:
            max_v = total
        total = 0


    print('#{} {}'.format(tn, max_v))