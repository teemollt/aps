import sys
sys.stdin = open("sample_input (1).txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                arr[j][k] += color
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] > 2:
                cnt += 1

    print('#{} {}'.format(tc, cnt))