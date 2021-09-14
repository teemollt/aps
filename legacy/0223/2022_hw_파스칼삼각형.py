import sys
sys.stdin = open("input (hw3).txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # n줄 필요
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        # i 까지만 필요
        for j in range(i+1):
            # 맨 왼쪽 or 맨오른쪽은 1
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                # (i,j)는 (i-1, j) + (i-1, j-1)
                if i > 0 and j > 0:
                    arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()