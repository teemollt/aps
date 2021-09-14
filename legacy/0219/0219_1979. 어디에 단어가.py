import sys
sys.stdin = open("input (1979).txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 연속된 k개 만큼의 1을 찾찾
    cnt = 0
    for i in range(n):
        tmp = []
        for j in range(n-m+1):
            for x in range(m+2):
                tmp.append(arr[i][j])
            if tmp == [1, 1, 1]:
                cnt += 1
    # for i in range(n):
    #     tmp = []
    #     for j in range(n-m+1):
    #         for x in range(m):
    #             tmp.append(arr[j][i])
    #         if tmp == [1, 1, 1]:
    #             cnt += 1

    print(cnt)