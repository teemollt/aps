# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
# print(arr)
c = [[""] * 8 for _ in range(8)]
d = [[""] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i % 2:
            if j % 2:
                c[i][j] = "B"
                d[i][j] = "W"
            else:
                c[i][j] = "W"
                d[i][j] = "B"
        else:
            if j % 2:
                c[i][j] = "W"
                d[i][j] = "B"
            else:
                c[i][j] = "B"
                d[i][j] = "W"

min_c = 987654321
min_d = 987654321
for i in range(0, n-7):
    for j in range(0, m-7):
        cnt_c = 0
        cnt_d = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if arr[x][y] != c[x-i][y-j]:
                    cnt_c += 1
                if arr[x][y] != d[x-i][y-j]:
                    cnt_d += 1
        if cnt_c < min_c:
            min_c = cnt_c
        if cnt_d < min_d:
            min_d = cnt_d
print(min(min_c, min_d))

